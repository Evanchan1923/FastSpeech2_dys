import io
import json
import re
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
from scipy.io import wavfile
from tqdm import tqdm

from text import _clean_text


TEXT_FIELD_FALLBACKS = [
    "norm_text_without_disfluency_team",
    "norm_text_without_disfluency",
    "norm_text_with_disfluency_team",
    "norm_text_with_disfluency",
    "text",
]


def _sanitize(value, default):
    value = str(value or default)
    value = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return value or default


def get_speaker_filter(config):
    speaker_filter = config.get("speaker_filter") or config.get("speakers")
    if speaker_filter in (None, "", []):
        return None
    if isinstance(speaker_filter, str):
        return {speaker_filter}
    return {str(speaker) for speaker in speaker_filter}


def _load_dataset(path, split):
    try:
        from datasets import Audio, DatasetDict, load_dataset, load_from_disk
    except ImportError as exc:
        raise ImportError(
            "SAPC HuggingFace preprocessing requires the 'datasets' package. "
            "Install it in the FastSpeech_tts environment."
        ) from exc

    path = Path(path)
    candidates = [path]
    if path.name == split:
        candidates.append(path.parent)

    last_error = None
    for candidate in candidates:
        try:
            dataset = load_from_disk(str(candidate))
            if isinstance(dataset, DatasetDict):
                if split in dataset:
                    return _disable_audio_decoding(dataset[split], Audio)
                return _disable_audio_decoding(dataset[next(iter(dataset.keys()))], Audio)
            return _disable_audio_decoding(dataset, Audio)
        except Exception as exc:  # datasets raises several format-specific errors
            last_error = exc

    data_files = []
    for pattern in ("*.parquet", "*.jsonl", "*.json", "*.csv"):
        data_files.extend(str(p) for p in path.glob(pattern))
    if data_files:
        suffix = Path(data_files[0]).suffix
        loader = {
            ".parquet": "parquet",
            ".jsonl": "json",
            ".json": "json",
            ".csv": "csv",
        }[suffix]
        return _disable_audio_decoding(
            load_dataset(loader, data_files=data_files, split="train"), Audio
        )

    raise RuntimeError(
        "Could not load HuggingFace dataset from '{}'. Last load_from_disk error: {}"
        .format(path, last_error)
    )


def _disable_audio_decoding(dataset, audio_feature):
    if "audio" not in getattr(dataset, "column_names", []):
        return dataset

    feature = dataset.features.get("audio")
    if feature.__class__.__name__ != "Audio":
        return dataset

    # Avoid HF audio decoding dependencies; _load_audio reads bytes/path/array itself.
    return dataset.cast_column("audio", audio_feature(decode=False))


def _choose_text(row, text_field, cleaners):
    fields = [text_field] if text_field else []
    fields.extend(field for field in TEXT_FIELD_FALLBACKS if field not in fields)
    for field in fields:
        text = row.get(field)
        if text is not None and str(text).strip():
            return _clean_text(str(text).strip(), cleaners)
    return None


def _resolve_audio_path(path, dataset_root):
    if not path:
        return None
    path = Path(path)
    if path.is_absolute():
        return path

    candidates = [
        dataset_root / path,
        dataset_root.parent / path,
        dataset_root.parent.parent / path,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return dataset_root / path


def _load_audio(row, dataset_root, sampling_rate):
    audio = row.get("audio")

    if isinstance(audio, dict) and audio.get("bytes") is not None:
        with io.BytesIO(audio["bytes"]) as bio:
            wav, source_sr = sf.read(bio, dtype="float32", always_2d=False)
    elif isinstance(audio, dict) and audio.get("array") is not None:
        wav = np.asarray(audio["array"], dtype=np.float32)
        source_sr = int(audio.get("sampling_rate") or sampling_rate)
    else:
        audio_path = row.get("audio_filepath")
        if not audio_path and isinstance(audio, dict):
            audio_path = audio.get("path")
        audio_path = _resolve_audio_path(audio_path, dataset_root)
        if audio_path is None or not audio_path.exists():
            raise FileNotFoundError(
                "Missing audio file for row id {}".format(row.get("id"))
            )
        wav, source_sr = sf.read(str(audio_path), dtype="float32", always_2d=False)

    wav = np.asarray(wav, dtype=np.float32)
    if wav.ndim == 2:
        wav = wav.mean(axis=1)
    if source_sr != sampling_rate:
        wav = librosa.resample(wav, source_sr, sampling_rate)
    return np.asarray(wav, dtype=np.float32)


def _normalize_wav(wav, max_wav_value):
    wav = np.asarray(wav, dtype=np.float32)
    peak = np.max(np.abs(wav)) if wav.size else 0.0
    if peak > 0:
        wav = wav / peak * max_wav_value
    return wav.astype(np.int16)


def prepare_align(config):
    dataset_root = Path(config["path"]["corpus_path"])
    out_dir = Path(config["path"]["raw_path"])
    sapc_config = config.get("sapc_hf", {})
    split = sapc_config.get("split", "train")
    text_field = sapc_config.get("text_field", "norm_text_without_disfluency")
    id_field = sapc_config.get("id_field", "id")
    speaker_field = sapc_config.get("speaker_field", "speaker")
    speaker_filter = get_speaker_filter(sapc_config)

    sampling_rate = config["preprocessing"]["audio"]["sampling_rate"]
    max_wav_value = config["preprocessing"]["audio"]["max_wav_value"]
    cleaners = config["preprocessing"]["text"]["text_cleaners"]

    dataset = _load_dataset(dataset_root, split)
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = out_dir / "sapc_hf_manifest.jsonl"
    written = 0
    skipped = 0
    seen = set()

    with open(manifest_path, "w", encoding="utf-8") as manifest:
        for index in tqdm(range(len(dataset)), desc="Preparing SAPC HF"):
            row = dataset[index]
            speaker = str(row.get(speaker_field) or "")
            if speaker_filter is not None and speaker not in speaker_filter:
                skipped += 1
                continue

            text = _choose_text(row, text_field, cleaners)
            if text is None:
                skipped += 1
                continue

            speaker = _sanitize(speaker, "speaker_0")
            basename = _sanitize(row.get(id_field), "utt_{:08d}".format(index))
            if (speaker, basename) in seen:
                basename = "{}_{:08d}".format(basename, index)
            seen.add((speaker, basename))

            wav = _load_audio(row, dataset_root, sampling_rate)
            speaker_dir = out_dir / speaker
            speaker_dir.mkdir(parents=True, exist_ok=True)

            wavfile.write(
                speaker_dir / "{}.wav".format(basename),
                sampling_rate,
                _normalize_wav(wav, max_wav_value),
            )
            with open(
                speaker_dir / "{}.lab".format(basename), "w", encoding="utf-8"
            ) as lab_file:
                lab_file.write(text)

            manifest.write(
                json.dumps(
                    {
                        "id": row.get(id_field),
                        "speaker": row.get(speaker_field),
                        "basename": basename,
                        "raw_text": row.get("text"),
                        "lab_text": text,
                        "audio_filepath": row.get("audio_filepath"),
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
            written += 1

    if written == 0:
        raise RuntimeError(
            "No SAPC HuggingFace rows were converted. Check corpus_path and text fields."
        )

    print(
        "Prepared {} utterances in {}. Skipped {} rows.".format(
            written, out_dir, skipped
        )
    )
