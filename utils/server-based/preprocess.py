import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from speech.preprocessor.preprocessor import Preprocessor
from utils.config import load_preprocess_config


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="path to preprocess.yaml")
    args = parser.parse_args()

    config = load_preprocess_config(args.config)
    preprocessor = Preprocessor(config)
    preprocessor.build_from_path()
