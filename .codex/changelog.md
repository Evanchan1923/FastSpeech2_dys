# Changelog

## 2026-07-05

- Switched the documented Katana runtime from a Python venv to the `FastSpeech_tts` conda environment.
- Renamed the PBS setup guide to `docs/PBS_CONDA_SETUP.md` and updated README links.
- Removed stale `run.venv_dir` entries from the SAPC v1/v2 YAML configs because the PBS script now activates conda directly.
- Kept MFA out of `requirements.txt`; MFA is provided by the conda environment.
- Tightened the PBS MFA preflight so a broken `mfa version` stops before data preparation.
- Trimmed non-essential PBS diagnostics while keeping the conda activation and MFA startup preflight.
- Fixed SAPC audio resampling with newer `librosa` by passing `orig_sr` and `target_sr` as keyword arguments.
- Kept `fastspeech2_v1.log` tracked as the current server run diagnostic log.
- Aligned v1 YAML `omp_num_threads` with the one-CPU `fastSpeech2_v1.pbs` allocation before resubmission.
- Added an MFA/Kalpy compatibility preflight for the `use_g2p` graph-compiler API mismatch.
- Updated the conda setup smoke test with the same MFA/Kalpy check and repair command.
- Limited MFA alignment jobs to the configured runtime CPU count.

## 2026-07-04

- Added pip/venv MFA setup notes to `docs/PBS_VENV_SETUP.md`.
- Added a PBS preflight check that reports the MFA executable/version and fails before data preparation if `mfa` is missing.
- Tested pip/venv MFA dependency pins before switching the Katana runtime to conda-provided MFA.
- Pinned `setuptools==68.2.2` so `librosa` can import `pkg_resources` at runtime in the server venv.
- Added a `pkg_resources` repair command to `docs/PBS_VENV_SETUP.md`.
- Added `config/SAPC_subset001/fastSpeech2_v2.yaml` for true multi-speaker SAPC training and `fastSpeech2_v2.pbs` to submit it.
- Updated v2 to use a single `run.speakers` list for selected-speaker multi-speaker training and generation.
- Updated the PBS setup smoke test to validate both v1 per-speaker and v2 selected-speaker multi-speaker configs.
- Updated pretrained checkpoint loading so multi-speaker models can initialize from compatible single-speaker checkpoint weights while randomly initializing incompatible layers.
- Reordered `config/SAPC_subset001/fastSpeech2_v1.yaml` so CPU/GPU settings and path-heavy settings are at the top.
- Added concise comments for non-obvious YAML settings such as runtime resources, auto-resume, sample-rate compatibility, and loss reporting cadence.
- Moved runtime CPU/GPU settings under `train.resources` and removed the duplicate `data_loader_num_workers` setting.
- Removed default `restore_step: "latest"` and `logging.use_vocoder: True` entries from the SAPC YAML; those defaults now live in the scripts.

## 2026-07-03

- Merged the SAPC configs into `config/SAPC_subset001/fastSpeech2_v1.yaml` with `run`, `preprocess`, `train`, `gen`, and `model` sections.
- Updated SAPC PBS/script defaults to use the unified config file and removed the old SAPC split YAML files.
- Simplified SAPC runtime resource settings to CPU/GPU values used by Python; PBS scheduler resources remain in `fastSpeech2_v1.pbs`.
- Reordered `fastSpeech2_v1.yaml` so run controls and path-heavy sections are near the top, with model architecture settings at the bottom.
- Updated `requirements.txt` to Python 3.10-compatible package pins to avoid legacy NumPy/source-build failures during venv setup.
- Added automatic resume from the latest FastSpeech2 checkpoint, with fallback to step 0 plus pretrained initialization when no checkpoint exists.
- Added runtime CPU/GPU settings used by the PBS script and training job.
- Added configurable training report cadence via `step.report_step`, set to `5000` for SAPC.
- Added `docs/PBS_VENV_SETUP.md` with no-conda venv setup commands and a copy-paste PBS smoke test.
- Documented the updated training, resource, and setup workflow in README/config/pipeline docs.

## 2026-06-30

- Moved the pipeline summary into `docs/PIPELINE_SUMMARY.md`.
- Updated the README link to the moved pipeline summary.
- Moved lexicon files into `text/lexicon/` and updated preprocess configs.
- Grouped speech processing modules under `speech/` and updated imports/fallback paths.
- Added project context, decisions, lessons learned, and completed-task bookkeeping for the repository layout update.
