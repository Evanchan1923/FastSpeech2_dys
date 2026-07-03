# Done

## 2026-07-03

- Merged the SAPC split YAML configs into `config/SAPC_subset001/fastSpeech2_v1.yaml` and removed the old SAPC `preprocess.yaml`, `model.yaml`, `train.yaml`, `gen.yaml`, `run.yaml`, and `resources.yaml` files.
- Updated the config loader and PBS/script defaults so SAPC stages can read the unified config sections while legacy split YAML files still work.
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
