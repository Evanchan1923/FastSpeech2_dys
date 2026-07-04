# PBS Venv Setup

Use these commands on the server from the repository root. They create the Python
venv used by `config/SAPC_subset001/fastSpeech2_v1.yaml` and `fastSpeech2_v1.pbs`.
The PBS script activates this default venv before reading YAML configs, so keep
`run.venv_dir` pointed here unless you also update `DEFAULT_VENV_DIR` for the
job.
The same venv is used by `fastSpeech2_v2.pbs` for the multi-speaker config.

## 1. Create The Venv

```bash
cd /path/to/FastSpeech2_dys

module load python/3.10.8
module load ffmpeg/7.0.2
module load cuda/12.1.1

rm -rf /srv/scratch/z5327748/venv/FastSpeech_tts
python -m venv /srv/scratch/z5327748/venv/FastSpeech_tts
source /srv/scratch/z5327748/venv/FastSpeech_tts/bin/activate

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python -m pip check
```

The requirements are pinned for `python/3.10.8`. If pip previously failed while
building old NumPy from source, remove the venv and recreate it with the commands
above so the updated Python 3.10 wheels are installed into a clean environment.

## 2. Confirm The Run Config

Edit:

```text
config/SAPC_subset001/fastSpeech2_v1.yaml
```

Set:

```yaml
run:
  speaker: "<speaker_id>"
```

Training auto-resume is the default. The job resumes the newest checkpoint in
the checkpoint directory. If no checkpoint exists, it starts from step 0 and
uses `pretrained_checkpoint` if that path is set.

## 3. Confirm CPU/GPU Settings

Edit:

```text
config/SAPC_subset001/fastSpeech2_v1.yaml
```

Keep these values matched with the PBS header or with the `qsub -l` resources
you request. The PBS scheduler request itself remains in `fastSpeech2_v1.pbs`.

```yaml
train:
  resources:
    ncpu: 2
    ngpu: 2
  data_loader:
    num_workers: 2
```

The training script uses DataParallel when more than one visible GPU is
requested.

## 4. Smoke-Test The PBS Setup

Paste this after activating the venv:

```bash
python - <<'PY'
from pathlib import Path
import subprocess
import sys

from utils.config import load_config, load_configs

repo = Path.cwd()
config_path = repo / "config/SAPC_subset001/fastSpeech2_v1.yaml"

subprocess.run(["bash", "-n", "fastSpeech2_v1.pbs"], check=True)

run_config = load_config(config_path, "run")
preprocess_config, model_config, train_config = load_configs(
    config_path,
    config_path,
    config_path,
)

speaker = str(run_config.get("speaker", "")).strip()
if speaker in ("", "CHANGE_ME", "<speaker_id>"):
    raise SystemExit("Set run.speaker in config/SAPC_subset001/fastSpeech2_v1.yaml before qsub.")

import torch

ckpt_dir = Path(train_config["path"]["ckpt_path"])
steps = []
if ckpt_dir.exists():
    for path in ckpt_dir.glob("*.pth.tar"):
        try:
            steps.append(int(path.name.split(".")[0]))
        except ValueError:
            pass

print("Python:", sys.version.split()[0])
print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA device count:", torch.cuda.device_count())
print("Speaker:", speaker)
print("Runtime ncpu:", train_config.get("resources", {}).get("ncpu"))
print("Runtime ngpu:", train_config.get("resources", {}).get("ngpu"))
print("Checkpoint dir:", ckpt_dir)
print("Latest checkpoint:", max(steps) if steps else "none; training will start at step 0")
print("PBS syntax/config smoke test passed.")
PY
```
