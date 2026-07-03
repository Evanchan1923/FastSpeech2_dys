# Changelog

## 2026-07-03

- Merged the SAPC configs into `config/SAPC_subset001/fastSpeech2_v1.yaml` with `run`, `resources`, `preprocess`, `model`, `train`, and `gen` sections.
- Updated SAPC PBS/script defaults to use the unified config file and removed the old SAPC split YAML files.
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
