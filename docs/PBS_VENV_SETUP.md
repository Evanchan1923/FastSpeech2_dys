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

For `fastSpeech2_v2.yaml`, set the selected multi-speaker subset instead:

```yaml
run:
  speakers:
    - "<speaker_id>"
    - "<speaker_id>"
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
jobs = [
    (
        "v1-per-speaker",
        repo / "config/SAPC_subset001/fastSpeech2_v1.yaml",
        repo / "fastSpeech2_v1.pbs",
    ),
    (
        "v2-multi-speaker",
        repo / "config/SAPC_subset001/fastSpeech2_v2.yaml",
        repo / "fastSpeech2_v2.pbs",
    ),
]

import torch

for label, config_path, pbs_path in jobs:
    subprocess.run(["bash", "-n", str(pbs_path)], check=True)

    run_config = load_config(config_path, "run")
    preprocess_config, model_config, train_config = load_configs(
        config_path,
        config_path,
        config_path,
    )
    gen_config = load_config(config_path, "gen")

    if model_config.get("multi_speaker", False):
        speakers = run_config.get("speakers") or []
        if not speakers:
            raise SystemExit("Set run.speakers in {} before qsub.".format(config_path))
        speaker_summary = "subset: {}".format(", ".join(str(s) for s in speakers))
        if preprocess_config.get("sapc_hf", {}).get("speaker_filter") != speakers:
            raise SystemExit("{} preprocess speaker_filter does not match run.speakers.".format(label))
        if gen_config.get("source", {}).get("speaker_filter") != speakers:
            raise SystemExit("{} generation speaker_filter does not match run.speakers.".format(label))
    else:
        speaker = str(run_config.get("speaker", "")).strip()
        if speaker in ("", "CHANGE_ME", "<speaker_id>"):
            raise SystemExit("Set run.speaker in {} before qsub.".format(config_path))
        speaker_summary = speaker

    ckpt_dir = Path(train_config["path"]["ckpt_path"])
    steps = []
    if ckpt_dir.exists():
        for path in ckpt_dir.glob("*.pth.tar"):
            try:
                steps.append(int(path.name.split(".")[0]))
            except ValueError:
                pass

    print("[{}] config: {}".format(label, config_path))
    print("[{}] pbs: {}".format(label, pbs_path))
    print("[{}] multi_speaker: {}".format(label, model_config.get("multi_speaker", False)))
    print("[{}] speaker(s): {}".format(label, speaker_summary))
    print("[{}] runtime ncpu: {}".format(label, train_config.get("resources", {}).get("ncpu")))
    print("[{}] runtime ngpu: {}".format(label, train_config.get("resources", {}).get("ngpu")))
    print("[{}] checkpoint dir: {}".format(label, ckpt_dir))
    print("[{}] latest checkpoint: {}".format(label, max(steps) if steps else "none; training will start at step 0"))

print("Python:", sys.version.split()[0])
print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA device count:", torch.cuda.device_count())
print("PBS syntax/config smoke tests passed.")
PY
```
