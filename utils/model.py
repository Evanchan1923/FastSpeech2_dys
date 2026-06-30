import os
import json
from pathlib import Path
from zipfile import ZipFile

import torch
import numpy as np

import speech.hifigan as hifigan
from model import FastSpeech2, ScheduledOptim


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_ROOT = Path("/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model")
REPO_HIFIGAN_DIR = REPO_ROOT / "speech" / "hifigan"


def _hifigan_dirs():
    model_root = Path(os.environ.get("FASTSPEECH2_MODEL_ROOT", DEFAULT_MODEL_ROOT))
    dirs = [model_root / "hifigan", REPO_HIFIGAN_DIR]
    return list(dict.fromkeys(dirs))


def get_model(args, configs, device, train=False):
    (preprocess_config, model_config, train_config) = configs

    model = FastSpeech2(preprocess_config, model_config).to(device)
    pretrained_checkpoint = getattr(args, "pretrained_checkpoint", None)
    if pretrained_checkpoint:
        ckpt = torch.load(pretrained_checkpoint, map_location=device)
        model.load_state_dict(ckpt["model"])
        print("Loaded pretrained FastSpeech2 checkpoint: {}".format(pretrained_checkpoint))
    elif args.restore_step:
        ckpt_path = os.path.join(
            train_config["path"]["ckpt_path"],
            "{}.pth.tar".format(args.restore_step),
        )
        ckpt = torch.load(ckpt_path, map_location=device)
        model.load_state_dict(ckpt["model"])

    if train:
        scheduled_optim = ScheduledOptim(
            model, train_config, model_config, args.restore_step
        )
        if args.restore_step and not pretrained_checkpoint:
            scheduled_optim.load_state_dict(ckpt["optimizer"])
        model.train()
        return model, scheduled_optim

    model.eval()
    model.requires_grad_ = False
    return model


def get_param_num(model):
    num_param = sum(param.numel() for param in model.parameters())
    return num_param


def _resolve_hifigan_file(filename):
    for directory in _hifigan_dirs():
        path = directory / filename
        if path.exists():
            return path
    raise FileNotFoundError(
        "HiFi-GAN file not found. Expected one of: {}".format(
            ", ".join(str(directory / filename) for directory in _hifigan_dirs())
        )
    )


def _resolve_hifigan_checkpoint(filename):
    for directory in _hifigan_dirs():
        ckpt_path = directory / filename
        if ckpt_path.exists():
            return ckpt_path

        zip_path = Path(str(ckpt_path) + ".zip")
        if zip_path.exists():
            print("Extracting HiFi-GAN checkpoint: {}".format(zip_path))
            with ZipFile(zip_path, "r") as zf:
                member = next(
                    (
                        name
                        for name in zf.namelist()
                        if Path(name).name == ckpt_path.name and not name.endswith("/")
                    ),
                    None,
                )
                if member is None:
                    raise FileNotFoundError(
                        "Could not find {} inside {}".format(ckpt_path.name, zip_path)
                    )
                zf.extract(member, directory)
                extracted_path = directory / member
                if extracted_path != ckpt_path:
                    extracted_path.replace(ckpt_path)
            return ckpt_path

    raise FileNotFoundError(
        "HiFi-GAN checkpoint not found. Expected one of: {}".format(
            ", ".join(
                "{} or {}".format(
                    directory / filename, Path(str(directory / filename) + ".zip")
                )
                for directory in _hifigan_dirs()
            )
        )
    )


def get_vocoder(config, device):
    name = config["vocoder"]["model"]
    speaker = config["vocoder"]["speaker"]

    if name is None or str(name).lower() == "none":
        return None

    if name == "MelGAN":
        if speaker == "LJSpeech":
            vocoder = torch.hub.load(
                "descriptinc/melgan-neurips", "load_melgan", "linda_johnson"
            )
        elif speaker == "universal":
            vocoder = torch.hub.load(
                "descriptinc/melgan-neurips", "load_melgan", "multi_speaker"
            )
        vocoder.mel2wav.eval()
        vocoder.mel2wav.to(device)
    elif name == "HiFi-GAN":
        with open(_resolve_hifigan_file("config.json"), "r", encoding="utf-8") as f:
            hifigan_config = json.load(f)
        hifigan_config = hifigan.AttrDict(hifigan_config)
        vocoder = hifigan.Generator(hifigan_config)
        if speaker == "LJSpeech":
            ckpt_path = _resolve_hifigan_checkpoint("generator_LJSpeech.pth.tar")
        elif speaker == "universal":
            ckpt_path = _resolve_hifigan_checkpoint("generator_universal.pth.tar")
        else:
            raise ValueError("Unsupported HiFi-GAN speaker: {}".format(speaker))
        ckpt = torch.load(ckpt_path, map_location=device)
        vocoder.load_state_dict(ckpt["generator"])
        vocoder.eval()
        vocoder.remove_weight_norm()
        vocoder.to(device)
    else:
        raise ValueError("Unsupported vocoder: {}".format(name))

    return vocoder


def vocoder_infer(mels, vocoder, model_config, preprocess_config, lengths=None):
    name = model_config["vocoder"]["model"]
    with torch.no_grad():
        if name == "MelGAN":
            wavs = vocoder.inverse(mels / np.log(10))
        elif name == "HiFi-GAN":
            wavs = vocoder(mels).squeeze(1)

    wavs = (
        wavs.cpu().numpy()
        * preprocess_config["preprocessing"]["audio"]["max_wav_value"]
    ).astype("int16")
    wavs = [wav for wav in wavs]

    for i in range(len(mels)):
        if lengths is not None:
            wavs[i] = wavs[i][: lengths[i]]

    return wavs
