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
- Diagnosed the next `fastspeech2_v1.log`: SAPC preparation completed and MFA failed during graph compilation due to an MFA/Kalpy `use_g2p` API mismatch.
- Added a PBS preflight and setup-doc smoke check for the MFA/Kalpy graph compiler signature, with the conda update command to repair the environment.
- Passed `--num_jobs` to MFA from the configured runtime CPU count so MFA does not exceed the PBS CPU allocation.
- Confirmed the next `fastspeech2_v1.log` stopped early at the new MFA/Kalpy preflight, before expensive SAPC preparation or MFA alignment.
- Corrected the MFA/Kalpy repair command from `conda update` to `conda install` because the CPU Kaldi build selector is an install spec.
- Relaxed the MFA/Kalpy preflight for MFA 3.4.0 so it only rejects environments where MFA actually passes `use_g2p` into Kalpy's graph compiler.
- Diagnosed the next `fastspeech2_v1.log`: MFA completed and exported 449 TextGrids, then preprocessing failed on newer `librosa.util.pad_center` keyword-only arguments.
- Updated audio preprocessing/STFT `librosa` calls to use keyword arguments for `pad_center`, mel filter construction, and legacy dataset audio loading.
- Optimized durable memory to reflect the current MFA 3.4.0 compatibility preflight and keyword-only-safe `librosa` preprocessing.
- Diagnosed the next `fastspeech2_v1.log`: MFA completed again, then preprocessing tried to treat `sapc_hf_manifest.jsonl` in `raw_path` as a speaker directory.
- Updated preprocessing to iterate only real speaker directories under `raw_path`.
- Diagnosed the next full-from-beginning `fastspeech2_v1.log`: prepare-align and MFA ran from scratch, but MFA exported TextGrids directly into `preprocessed_path` while preprocessing expects `preprocessed_path/TextGrid/<speaker>`.
- Updated `fastSpeech2_v1.pbs` to send MFA output to `${PREPROCESSED_PATH}/TextGrid` and fail early if MFA produces no `.TextGrid` files.

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
