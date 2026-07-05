# Decisions

## 2026-07-05

- Use the Katana `FastSpeech_tts` conda environment for Python, MFA, preprocessing, training, and generation; do not keep Python venv settings in SAPC YAML.
- Keep conda activation in `fastSpeech2_v1.pbs` through `CONDA_SH` and `CONDA_ENV_NAME` so v1 and the v2 wrapper share one environment path.

## 2026-07-04

- Add v2 as true multi-speaker training rather than cascaded per-speaker fine-tuning; keep cascade orchestration out of the model YAML.
- Use `run.speakers` in v2 as the single selected-speaker list, referenced by both train preprocessing and dev generation filters.
- Use a thin `fastSpeech2_v2.pbs` wrapper around the shared v1 PBS pipeline so stage logic stays in one place.
- Keep `fastSpeech2_v1.yaml` optimized for server editing: run paths/controls and path-heavy sections first, training runtime resources under `train.resources`, and lower-touch model settings last.
- Use comments only for non-obvious SAPC config choices; avoid explaining common dataset/path fields inline.

## 2026-07-03

- Use `config/SAPC_subset001/fastSpeech2_v1.yaml` as the single SAPC config file, with named sections for run controls, preprocessing, training, generation, and model settings.
- Order `fastSpeech2_v1.yaml` for server editing: run controls and path-heavy sections first, training runtime resources under `train.resources`, with lower-touch model architecture details last.
- Keep the config loader backward-compatible with legacy split files by returning a named section only when that section exists.
- Use code-level `"latest"` as the SAPC restore default so qsub jobs resume the newest checkpoint automatically and start from step 0 only when no run checkpoint exists.
- When both a run checkpoint and `pretrained_checkpoint` are configured, prefer the run checkpoint and restore its optimizer state; use `pretrained_checkpoint` only for step-0 initialization.
- Keep PBS scheduler directives explicit in `fastSpeech2_v1.pbs`; use `train.resources` only for runtime CPU/GPU settings that the training script needs.
- Use `step.report_step` as the new training loss/report cadence knob while preserving existing `log_step` as a fallback for older configs.
- Keep default restore behavior out of SAPC YAML: training and generation default to the latest checkpoint in code, and training vocoder logging defaults to enabled.

## 2026-06-30

- Use `speech/` as the parent package for the former root-level `audio`, `hifigan`, and `preprocessor` modules.
- Update code imports to explicit `speech.*` paths instead of keeping root-level compatibility packages.
- Keep the external model-root HiFi-GAN lookup at `<FASTSPEECH2_MODEL_ROOT>/hifigan`, while moving the repo-local fallback to `speech/hifigan`.
