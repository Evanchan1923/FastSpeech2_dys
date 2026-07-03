# Decisions

## 2026-07-03

- Use `config/SAPC_subset001/fastSpeech2_v1.yaml` as the single SAPC config file, with named sections for run controls, resources, preprocessing, model, training, and generation.
- Keep the config loader backward-compatible with legacy split files by returning a named section only when that section exists.
- Use `training.restore_step: "latest"` as the SAPC default so qsub jobs resume the newest checkpoint automatically and start from step 0 only when no run checkpoint exists.
- When both a run checkpoint and `pretrained_checkpoint` are configured, prefer the run checkpoint and restore its optimizer state; use `pretrained_checkpoint` only for step-0 initialization.
- Keep PBS resource directives explicit, and use the unified config `resources` section for runtime CPU/GPU settings that the PBS script exports and checks against scheduler-provided values.
- Use `step.report_step` as the new training loss/report cadence knob while preserving existing `log_step` as a fallback for older configs.

## 2026-06-30

- Use `speech/` as the parent package for the former root-level `audio`, `hifigan`, and `preprocessor` modules.
- Update code imports to explicit `speech.*` paths instead of keeping root-level compatibility packages.
- Keep the external model-root HiFi-GAN lookup at `<FASTSPEECH2_MODEL_ROOT>/hifigan`, while moving the repo-local fallback to `speech/hifigan`.
