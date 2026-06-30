# Lessons Learned

## 2026-06-30

- When moving repository lexicons, update `path.lexicon_path` in every preprocess config so synthesis and generation continue to load pronunciations.
- When moving the speech component packages, check both import statements and filesystem fallback paths such as the repo-local HiFi-GAN asset directory.
