import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from speech.preprocessor import ljspeech, aishell3, libritts, sapc_hf
from utils.config import load_preprocess_config


def main(config):
    dataset = config["dataset"]
    if "SAPC" in dataset or "Dysarthric" in dataset:
        sapc_hf.prepare_align(config)
    elif "LJSpeech" in dataset:
        ljspeech.prepare_align(config)
    elif "AISHELL3" in dataset:
        aishell3.prepare_align(config)
    elif "LibriTTS" in dataset:
        libritts.prepare_align(config)
    else:
        raise NotImplementedError(
            "prepare_align is not implemented for dataset '{}'. "
            "Create raw_path speaker folders with .wav/.lab files, then provide "
            "TextGrid alignments under preprocessed_path/TextGrid, or add a "
            "dataset-specific adapter.".format(dataset)
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="path to preprocess.yaml")
    args = parser.parse_args()

    config = load_preprocess_config(args.config)
    main(config)
