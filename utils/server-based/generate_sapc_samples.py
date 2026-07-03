import argparse
import json
import os
import random
import re
import sys
from pathlib import Path
from string import punctuation
from types import SimpleNamespace

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import numpy as np
import torch
from g2p_en import G2p
from tqdm import tqdm

from speech.preprocessor.sapc_hf import (
    TEXT_FIELD_FALLBACKS,
    _load_dataset,
    _sanitize,
    get_speaker_filter,
)
from text import text_to_sequence
from utils.config import load_config, load_configs
from utils.model import get_model, get_vocoder
from utils.tools import pad_1D, synth_samples, to_device


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def _read_lexicon(path):
    lexicon = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = re.split(r"\s+", line.strip())
            if len(parts) > 1 and parts[0].lower() not in lexicon:
                lexicon[parts[0].lower()] = parts[1:]
    return lexicon


def _choose_text(row, text_field):
    fields = [text_field] if text_field else []
    fields.extend(field for field in TEXT_FIELD_FALLBACKS if field not in fields)
    for field in fields:
        text = row.get(field)
        if text is not None and str(text).strip():
            return str(text).strip(), field
    return None, None


def _preprocess_english(text, preprocess_config, lexicon, g2p):
    text = text.rstrip(punctuation)
    phones = []
    words = re.split(r"([,;.\-\?\!\s+])", text)
    for word in words:
        if word.lower() in lexicon:
            phones += lexicon[word.lower()]
        else:
            phones += [phone for phone in g2p(word) if phone != " "]
    phones = "{" + "}{".join(phones) + "}"
    phones = re.sub(r"\{[^\w\s]?\}", "{sp}", phones)
    phones = phones.replace("}{", " ")
    return np.array(
        text_to_sequence(
            phones, preprocess_config["preprocessing"]["text"]["text_cleaners"]
        )
    )


def _resolve_restore_step(value, ckpt_path):
    if isinstance(value, str) and value.lower() == "latest":
        checkpoints = []
        for path in Path(ckpt_path).glob("*.pth.tar"):
            if path.name.split(".")[0].isdigit():
                checkpoints.append(int(path.name.split(".")[0]))
        if not checkpoints:
            raise FileNotFoundError(
                "No numeric checkpoints found in {}".format(ckpt_path)
            )
        return max(checkpoints)
    return int(value)


def _select_indices(dataset_size, selection, seed):
    indices = list(range(dataset_size))
    if selection == "random":
        rng = random.Random(seed)
        rng.shuffle(indices)
    elif selection != "first":
        raise ValueError("Unsupported generation.selection: {}".format(selection))
    return indices


def _batchify(samples, batch_size):
    for start in range(0, len(samples), batch_size):
        batch = samples[start : start + batch_size]
        ids = [sample["id"] for sample in batch]
        raw_texts = [sample["raw_text"] for sample in batch]
        speakers = np.array([sample["speaker_id"] for sample in batch])
        texts = [sample["text"] for sample in batch]
        text_lens = np.array([text.shape[0] for text in texts])
        yield (
            ids,
            raw_texts,
            speakers,
            pad_1D(texts),
            text_lens,
            max(text_lens),
        )


def _build_samples(dataset, indices, configs, gen_config):
    preprocess_config, model_config, _ = configs
    generation_config = gen_config["generation"]
    source_config = gen_config["source"]
    text_field = source_config.get("text_field")
    id_field = source_config.get("id_field", "id")
    speaker_field = source_config.get("speaker_field", "speaker")
    speaker_filter = get_speaker_filter(source_config)
    skip_unknown = generation_config.get("skip_unknown_speakers", True)
    target_count = int(generation_config.get("sample_count", 100))

    speakers_path = Path(preprocess_config["path"]["preprocessed_path"]) / "speakers.json"
    with open(speakers_path, "r", encoding="utf-8") as f:
        speaker_map = json.load(f)

    language = preprocess_config["preprocessing"]["text"]["language"]
    if language != "en":
        raise NotImplementedError("SAPC generation currently supports English text only.")

    lexicon = _read_lexicon(preprocess_config["path"]["lexicon_path"])
    g2p = G2p()
    samples = []
    skipped = {"missing_text": 0, "unknown_speaker": 0, "empty_phones": 0}

    for dataset_index in tqdm(indices, desc="Preparing samples"):
        if len(samples) >= target_count:
            break

        row = dataset[dataset_index]
        speaker = str(row.get(speaker_field) or "")
        if speaker_filter is not None and speaker not in speaker_filter:
            continue

        text, used_text_field = _choose_text(row, text_field)
        if text is None:
            skipped["missing_text"] += 1
            continue

        if model_config["multi_speaker"]:
            if speaker not in speaker_map:
                if skip_unknown:
                    skipped["unknown_speaker"] += 1
                    continue
                raise KeyError("Unknown speaker in dev set: {}".format(speaker))
            speaker_id = speaker_map[speaker]
        else:
            speaker_id = 0

        phones = _preprocess_english(text, preprocess_config, lexicon, g2p)
        if len(phones) == 0:
            skipped["empty_phones"] += 1
            continue

        basename = _sanitize(row.get(id_field), "utt_{:08d}".format(dataset_index))
        sample_id = "{}_{:04d}_{}_{}".format(
            gen_config["output"].get("filename_prefix", "sapc_dev"),
            len(samples),
            _sanitize(speaker, "speaker"),
            basename,
        )
        samples.append(
            {
                "id": sample_id,
                "dataset_index": dataset_index,
                "source_id": row.get(id_field),
                "speaker": speaker,
                "speaker_id": speaker_id,
                "text": phones,
                "raw_text": text,
                "used_text_field": used_text_field,
            }
        )

    if len(samples) == 0:
        raise RuntimeError("No generation samples were prepared. Skipped: {}".format(skipped))

    return samples, skipped


def _write_manifest(path, samples, skipped, configs, gen_config, restore_step):
    preprocess_config, _, train_config = configs
    payload = {
        "restore_step": restore_step,
        "preprocessed_path": preprocess_config["path"]["preprocessed_path"],
        "ckpt_path": train_config["path"]["ckpt_path"],
        "sample_count": len(samples),
        "skipped": skipped,
        "samples": [
            {
                "output_id": sample["id"],
                "dataset_index": sample["dataset_index"],
                "source_id": sample["source_id"],
                "speaker": sample["speaker"],
                "speaker_id": sample["speaker_id"],
                "text": sample["raw_text"],
                "used_text_field": sample["used_text_field"],
            }
            for sample in samples
        ],
        "config": gen_config,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def main(args):
    configs = load_configs(args.preprocess_config, args.model_config, args.train_config)
    preprocess_config, model_config, train_config = configs
    gen_config = load_config(args.gen_config, "gen")

    restore_step = args.restore_step
    if restore_step is None:
        restore_step = gen_config["generation"].get("restore_step", "latest")
    restore_step = _resolve_restore_step(restore_step, train_config["path"]["ckpt_path"])

    source_config = gen_config["source"]
    dataset = _load_dataset(source_config["corpus_path"], source_config.get("split", "dev"))
    indices = _select_indices(
        len(dataset),
        gen_config["generation"].get("selection", "first"),
        int(gen_config["generation"].get("seed", 1234)),
    )
    samples, skipped = _build_samples(dataset, indices, configs, gen_config)

    output_dir = Path(train_config["path"]["result_path"]) / gen_config["output"].get(
        "subdir", "dev_samples"
    )
    if gen_config["output"].get("include_step_subdir", True):
        output_dir = output_dir / "step_{}".format(restore_step)
    output_dir.mkdir(parents=True, exist_ok=True)

    model_args = SimpleNamespace(restore_step=restore_step)
    model = get_model(model_args, configs, device, train=False)
    vocoder = get_vocoder(model_config, device)

    pitch_control = float(gen_config.get("control", {}).get("pitch", 1.0))
    energy_control = float(gen_config.get("control", {}).get("energy", 1.0))
    duration_control = float(gen_config.get("control", {}).get("duration", 1.0))

    for batch in tqdm(
        _batchify(samples, int(gen_config["generation"].get("batch_size", 8))),
        desc="Generating samples",
    ):
        batch = to_device(batch, device)
        with torch.no_grad():
            output = model(
                *(batch[2:]),
                p_control=pitch_control,
                e_control=energy_control,
                d_control=duration_control
            )
            synth_samples(
                batch,
                output,
                vocoder,
                model_config,
                preprocess_config,
                str(output_dir),
            )

    _write_manifest(
        output_dir / "manifest.json", samples, skipped, configs, gen_config, restore_step
    )
    print("Generated {} samples in {}".format(len(samples), output_dir))
    print("Skipped rows: {}".format(skipped))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--preprocess_config",
        default="config/SAPC_subset001/fastSpeech2_v1.yaml",
        help="path to preprocess.yaml or unified config",
    )
    parser.add_argument(
        "-m",
        "--model_config",
        default="config/SAPC_subset001/fastSpeech2_v1.yaml",
        help="path to model.yaml or unified config",
    )
    parser.add_argument(
        "-t",
        "--train_config",
        default="config/SAPC_subset001/fastSpeech2_v1.yaml",
        help="path to train.yaml or unified config",
    )
    parser.add_argument(
        "-g",
        "--gen_config",
        default="config/SAPC_subset001/fastSpeech2_v1.yaml",
        help="path to gen.yaml or unified config",
    )
    parser.add_argument(
        "--restore_step",
        default=None,
        help="checkpoint step to restore, or 'latest'",
    )
    main(parser.parse_args())
