import os

import yaml


MODEL_ROOT_ENV = "FASTSPEECH2_MODEL_ROOT"
RESULT_ROOT_ENV = "FASTSPEECH2_RESULT_ROOT"
WORK_ROOT_ENV = "FASTSPEECH2_WORK_ROOT"
RUN_NAME_ENV = "FASTSPEECH2_RUN_NAME"
LEGACY_DATA_ROOT_ENV = "FASTSPEECH2_DATA_ROOT"
DEFAULT_MODEL_ROOT = "/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model"
DEFAULT_RESULT_ROOT = "/srv/scratch/speechdata/jinghao/fastSpeech2_result"
DEFAULT_WORK_ROOT = (
    "/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_fastSpeech2TTS"
)


def _expand_paths(value):
    if isinstance(value, dict):
        return {k: _expand_paths(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand_paths(v) for v in value]
    if isinstance(value, str):
        return os.path.expanduser(os.path.expandvars(value))
    return value


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return _expand_paths(yaml.load(f, Loader=yaml.FullLoader))


def apply_runtime_overrides(preprocess_config, train_config=None):
    model_root = os.environ.get(MODEL_ROOT_ENV) or os.environ.get(LEGACY_DATA_ROOT_ENV)
    result_root = os.environ.get(RESULT_ROOT_ENV)
    work_root = os.environ.get(WORK_ROOT_ENV)
    if not model_root and not result_root and not work_root:
        return

    dataset = preprocess_config["dataset"]
    run_name = os.environ.get(RUN_NAME_ENV, dataset)
    pre_paths = preprocess_config.setdefault("path", {})
    if work_root:
        pre_paths["raw_path"] = os.environ.get(
            "FASTSPEECH2_RAW_PATH", os.path.join(work_root, "raw_data", run_name)
        )
        pre_paths["preprocessed_path"] = os.environ.get(
            "FASTSPEECH2_PREPROCESSED_PATH",
            os.path.join(work_root, "preprocessed_data", run_name),
        )
    if os.environ.get("FASTSPEECH2_CORPUS_PATH"):
        pre_paths["corpus_path"] = os.environ["FASTSPEECH2_CORPUS_PATH"]

    if train_config is None:
        return

    if not result_root:
        result_root = model_root
    if not result_root:
        return

    train_paths = train_config.setdefault("path", {})
    train_paths["ckpt_path"] = os.environ.get(
        "FASTSPEECH2_CKPT_PATH", os.path.join(result_root, "output", "ckpt", run_name)
    )
    train_paths["log_path"] = os.environ.get(
        "FASTSPEECH2_LOG_PATH", os.path.join(result_root, "output", "log", run_name)
    )
    train_paths["result_path"] = os.environ.get(
        "FASTSPEECH2_RESULT_PATH",
        os.path.join(result_root, "output", "result", run_name),
    )


def load_preprocess_config(path):
    config = load_config(path)
    apply_runtime_overrides(config)
    return config


def load_configs(preprocess_path, model_path, train_path):
    preprocess_config = load_config(preprocess_path)
    model_config = load_config(model_path)
    train_config = load_config(train_path)
    apply_runtime_overrides(preprocess_config, train_config)
    return preprocess_config, model_config, train_config
