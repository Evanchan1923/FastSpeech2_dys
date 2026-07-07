# Done

## 2026-07-05

- Updated PBS setup documentation for the Katana `FastSpeech_tts` conda environment.
- Updated README to link to `docs/PBS_CONDA_SETUP.md`.
- Removed unused `run.venv_dir` settings from SAPC v1/v2 configs.
- Kept MFA installation documented as conda-provided rather than pip-pinned in `requirements.txt`.
- Made the PBS MFA preflight fail fast when `mfa version` cannot start.
- Trimmed non-essential diagnostics from `fastSpeech2_v1.pbs` while keeping the MFA startup preflight.
- Diagnosed `fastspeech2_v1.log`: MFA starts, but the `english_mfa` acoustic model is missing from the active conda environment.
- Diagnosed the next MFA failure: `english_mfa` loads, but MFA/Kalpy appear version-incompatible during graph compilation and the repo Librispeech lexicon does not match the `english_mfa` phone set.
- Updated SAPC v1/v2 MFA configs to use the matching `english_us_mfa` dictionary model instead of the repo Librispeech lexicon.
- Diagnosed tracked `fastspeech2_v1.log`: alignment data preparation now reaches SAPC audio loading, then fails on the newer `librosa.resample` keyword-only API.
- Updated SAPC audio resampling to use `orig_sr` and `target_sr` keyword arguments for newer conda `librosa` versions.
- Confirmed `fastspeech2_v1.log` should remain tracked for server run diagnostics.
- Ran pre-qsub checks for v1/v2 PBS syntax, SAPC YAML shape, and the resampling call; aligned v1 `omp_num_threads` with its one-CPU PBS allocation.

## 2026-07-04

- Documented Montreal Forced Aligner installation for the SAPC PBS workflow.
- Added a `fastSpeech2_v1.pbs` preflight check for the configured MFA executable.
- Pinned MFA plus `kalpy-kaldi` for pip/venv installation and switched v1/v2 SAPC configs to venv `mfa` with the current `english_mfa` acoustic model name.
- Pinned `setuptools==68.2.2` in `requirements.txt` to provide `pkg_resources` for `librosa`.
- Added an existing-venv repair snippet for `ModuleNotFoundError: No module named 'pkg_resources'` to `docs/PBS_VENV_SETUP.md`.
- Added `config/SAPC_subset001/fastSpeech2_v2.yaml` for true multi-speaker SAPC training across a selected speaker subset.
- Updated v2 to train/generate only the speaker IDs listed once in `run.speakers`.
- Added `fastSpeech2_v2.pbs` as a PBS wrapper that submits the v2 multi-speaker config.
- Updated `docs/PBS_VENV_SETUP.md` smoke-test code to validate both v1 and v2 PBS/config pairs.
- Made pretrained checkpoint loading skip incompatible layers so a multi-speaker model can initialize from compatible single-speaker checkpoint weights.
- Reordered `config/SAPC_subset001/fastSpeech2_v1.yaml` so CPU/GPU, run path/control settings, and dataset/output paths appear before lower-touch training/model details.
- Added short comments for non-obvious SAPC YAML settings without commenting common dataset fields.
- Moved runtime CPU/GPU settings into `train.resources` and removed duplicate DataLoader worker configuration.
- Removed redundant SAPC YAML defaults for training/generation `restore_step: "latest"` and `logging.use_vocoder: True`; scripts provide those defaults.

## 2026-07-03

- Merged the SAPC split YAML configs into `config/SAPC_subset001/fastSpeech2_v1.yaml` and removed the old SAPC `preprocess.yaml`, `model.yaml`, `train.yaml`, `gen.yaml`, `run.yaml`, and `resources.yaml` files.
- Updated the config loader and PBS/script defaults so SAPC stages can read the unified config sections while legacy split YAML files still work.
- Simplified SAPC runtime resource settings to `ncpu`/`ngpu` while leaving scheduler resources in `fastSpeech2_v1.pbs`.
- Reordered `fastSpeech2_v1.yaml` to put run controls and path-heavy sections before lower-touch model settings.
- Updated Python dependencies for the documented Python 3.10 server venv after the old NumPy pin failed to build.
- Added automatic FastSpeech2 training resume with `restore_step: "latest"` / `"auto"` checkpoint discovery.
- Added SAPC PBS/runtime CPU and GPU settings and wired them into `fastSpeech2_v1.pbs`.
- Added `step.report_step: 5000` support for controlling training loss/report logging cadence.
- Added Python venv setup and PBS smoke-test documentation in `docs/PBS_VENV_SETUP.md`.
- Updated README, config docs, and pipeline summary for auto-resume, resource config, report cadence, and setup testing.

## 2026-06-30

- Captured the key SAPC FastSpeech2 pipeline context in `.codex/memory/project-context.md`.
- Moved `PIPELINE_SUMMARY.md` to `docs/PIPELINE_SUMMARY.md`.
- Moved repository lexicons to `text/lexicon/` and updated preprocess config paths.
- Grouped `audio`, `hifigan`, and `preprocessor` under `speech/` and updated imports and repo-local HiFi-GAN fallback paths.
