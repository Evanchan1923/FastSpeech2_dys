import argparse
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

from utils.model import get_model, get_vocoder, get_param_num
from utils.tools import to_device, log, synth_one_sample
from utils.config import load_configs
from model import FastSpeech2Loss
from dataset import Dataset

from evaluate import evaluate

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def resolve_restore_step(value, ckpt_path):
    if value is None:
        return 0
    if isinstance(value, int):
        return value

    value = str(value).strip().lower()
    if value in ("", "0", "none", "false"):
        return 0
    if value in ("latest", "auto"):
        checkpoints = []
        ckpt_dir = Path(ckpt_path)
        if ckpt_dir.exists():
            for path in ckpt_dir.glob("*.pth.tar"):
                try:
                    checkpoints.append(int(path.name.split(".")[0]))
                except ValueError:
                    continue
        if checkpoints:
            return max(checkpoints)
        print("No existing checkpoints found in {}; starting from step 0.".format(ckpt_path))
        return 0

    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(
            "--restore_step must be an integer step, 'latest', or 'auto'; got {!r}".format(value)
        ) from exc


def get_requested_ngpu(train_config):
    value = os.environ.get("FASTSPEECH2_NGPU")
    if value is None:
        value = train_config.get("resources", train_config.get("resource", {})).get("ngpu")
    if value in (None, ""):
        return None
    return max(0, int(value))


def get_num_workers(train_config):
    loader_config = train_config.get("data_loader", {})
    value = os.environ.get("FASTSPEECH2_NUM_WORKERS")
    if value is not None:
        return int(value)
    if "num_workers" in loader_config:
        return int(loader_config["num_workers"])
    ncpu = os.environ.get("FASTSPEECH2_NCPU") or train_config.get("resources", train_config.get("resource", {})).get("ncpu")
    if ncpu in (None, ""):
        return 0
    return max(0, int(ncpu) - 1)


def main(args, configs):
    print("Prepare training ...")

    preprocess_config, model_config, train_config = configs
    args.restore_step = resolve_restore_step(args.restore_step, train_config["path"]["ckpt_path"])

    # Get dataset
    dataset = Dataset(
        "train.txt", preprocess_config, train_config, sort=True, drop_last=True
    )
    batch_size = train_config["optimizer"]["batch_size"]
    group_size = 4  # Set this larger than 1 to enable sorting in Dataset
    if batch_size * group_size >= len(dataset):
        raise ValueError(
            "Training set is too small for batch_size={} and group_size={}; "
            "need more than {} samples but found {}.".format(
                batch_size, group_size, batch_size * group_size, len(dataset)
            )
        )
    loader_config = train_config.get("data_loader", {})
    num_workers = get_num_workers(train_config)
    pin_memory = bool(loader_config.get("pin_memory", torch.cuda.is_available()))
    data_loader_kwargs = {
        "batch_size": batch_size * group_size,
        "shuffle": True,
        "collate_fn": dataset.collate_fn,
        "num_workers": num_workers,
        "pin_memory": pin_memory,
    }
    if num_workers > 0:
        data_loader_kwargs["prefetch_factor"] = int(
            loader_config.get("prefetch_factor", 2)
        )
    loader = DataLoader(
        dataset,
        **data_loader_kwargs,
    )

    # Prepare model
    model, optimizer = get_model(args, configs, device, train=True)
    requested_ngpu = get_requested_ngpu(train_config)
    available_ngpu = torch.cuda.device_count()
    if requested_ngpu is not None and requested_ngpu > available_ngpu:
        raise RuntimeError(
            "Requested {} GPU(s), but PyTorch can see only {} GPU(s).".format(
                requested_ngpu, available_ngpu
            )
        )
    data_parallel_ngpu = requested_ngpu if requested_ngpu is not None else available_ngpu
    if data_parallel_ngpu > 1:
        model = nn.DataParallel(model, device_ids=list(range(data_parallel_ngpu)))
        print("Using DataParallel on {} GPU(s).".format(data_parallel_ngpu))
    elif available_ngpu:
        print("Using 1 GPU.")
    else:
        print("Using CPU.")
    num_param = get_param_num(model)
    Loss = FastSpeech2Loss(preprocess_config, model_config).to(device)
    print("Number of FastSpeech2 Parameters:", num_param)

    # Load vocoder
    use_vocoder = train_config.get("logging", {}).get("use_vocoder", True)
    vocoder = get_vocoder(model_config, device) if use_vocoder else None

    # Init logger
    for p in train_config["path"].values():
        os.makedirs(p, exist_ok=True)
    train_log_path = os.path.join(train_config["path"]["log_path"], "train")
    val_log_path = os.path.join(train_config["path"]["log_path"], "val")
    os.makedirs(train_log_path, exist_ok=True)
    os.makedirs(val_log_path, exist_ok=True)
    train_logger = SummaryWriter(train_log_path)
    val_logger = SummaryWriter(val_log_path)

    # Training
    step = args.restore_step + 1
    epoch = 1
    grad_acc_step = train_config["optimizer"]["grad_acc_step"]
    grad_clip_thresh = train_config["optimizer"]["grad_clip_thresh"]
    total_step = train_config["step"]["total_step"]
    report_step = int(train_config["step"].get("report_step", train_config["step"].get("log_step", 100)))
    save_step = train_config["step"]["save_step"]
    synth_step = train_config["step"]["synth_step"]
    val_step = train_config["step"]["val_step"]

    outer_bar = tqdm(total=total_step, desc="Training", position=0)
    outer_bar.n = args.restore_step
    outer_bar.update()

    while True:
        inner_bar = tqdm(total=len(loader), desc="Epoch {}".format(epoch), position=1)
        for batchs in loader:
            for batch in batchs:
                batch = to_device(batch, device)

                # Forward
                output = model(*(batch[2:]))

                # Cal Loss
                losses = Loss(batch, output)
                total_loss = losses[0]

                # Backward
                total_loss = total_loss / grad_acc_step
                total_loss.backward()
                if step % grad_acc_step == 0:
                    # Clipping gradients to avoid gradient explosion
                    nn.utils.clip_grad_norm_(model.parameters(), grad_clip_thresh)

                    # Update weights
                    optimizer.step_and_update_lr()
                    optimizer.zero_grad()

                if step % report_step == 0:
                    losses = [l.item() for l in losses]
                    message1 = "Step {}/{}, ".format(step, total_step)
                    message2 = "Total Loss: {:.4f}, Mel Loss: {:.4f}, Mel PostNet Loss: {:.4f}, Pitch Loss: {:.4f}, Energy Loss: {:.4f}, Duration Loss: {:.4f}".format(
                        *losses
                    )

                    with open(os.path.join(train_log_path, "log.txt"), "a") as f:
                        f.write(message1 + message2 + "\n")

                    outer_bar.write(message1 + message2)

                    log(train_logger, step, losses=losses)

                if step % synth_step == 0:
                    fig, wav_reconstruction, wav_prediction, tag = synth_one_sample(
                        batch,
                        output,
                        vocoder,
                        model_config,
                        preprocess_config,
                    )
                    log(
                        train_logger,
                        fig=fig,
                        tag="Training/step_{}_{}".format(step, tag),
                    )
                    sampling_rate = preprocess_config["preprocessing"]["audio"][
                        "sampling_rate"
                    ]
                    log(
                        train_logger,
                        audio=wav_reconstruction,
                        sampling_rate=sampling_rate,
                        tag="Training/step_{}_{}_reconstructed".format(step, tag),
                    )
                    log(
                        train_logger,
                        audio=wav_prediction,
                        sampling_rate=sampling_rate,
                        tag="Training/step_{}_{}_synthesized".format(step, tag),
                    )

                if step % val_step == 0:
                    model.eval()
                    message = evaluate(model, step, configs, val_logger, vocoder)
                    with open(os.path.join(val_log_path, "log.txt"), "a") as f:
                        f.write(message + "\n")
                    outer_bar.write(message)

                    model.train()

                if step % save_step == 0:
                    model_state = (
                        model.module.state_dict()
                        if isinstance(model, nn.DataParallel)
                        else model.state_dict()
                    )
                    torch.save(
                        {
                            "model": model_state,
                            "optimizer": optimizer._optimizer.state_dict(),
                        },
                        os.path.join(
                            train_config["path"]["ckpt_path"],
                            "{}.pth.tar".format(step),
                        ),
                    )

                if step == total_step:
                    quit()
                step += 1
                outer_bar.update(1)

            inner_bar.update(1)
        epoch += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--restore_step", type=str, default="latest")
    parser.add_argument(
        "--pretrained_checkpoint",
        type=str,
        default=None,
        help="path to a compatible FastSpeech2 checkpoint for fine-tuning",
    )
    parser.add_argument(
        "-p",
        "--preprocess_config",
        type=str,
        required=True,
        help="path to preprocess.yaml or unified config",
    )
    parser.add_argument(
        "-m", "--model_config", type=str, required=True, help="path to model.yaml or unified config"
    )
    parser.add_argument(
        "-t", "--train_config", type=str, required=True, help="path to train.yaml or unified config"
    )
    args = parser.parse_args()

    # Read Config
    configs = load_configs(args.preprocess_config, args.model_config, args.train_config)

    main(args, configs)
