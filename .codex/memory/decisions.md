# Decisions

## 2026-06-30

- Use `speech/` as the parent package for the former root-level `audio`, `hifigan`, and `preprocessor` modules.
- Update code imports to explicit `speech.*` paths instead of keeping root-level compatibility packages.
- Keep the external model-root HiFi-GAN lookup at `<FASTSPEECH2_MODEL_ROOT>/hifigan`, while moving the repo-local fallback to `speech/hifigan`.
