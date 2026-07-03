# Lessons Learned

## 2026-07-03

- When consolidating YAML configs, add section extraction in the shared loader rather than teaching every caller a new file format.
- For fine-tuning configs that keep `pretrained_checkpoint` set, auto-resume must still prefer the run checkpoint and restore optimizer state, otherwise resumed jobs silently lose optimizer history.
- PBS `#PBS` directives are parsed before shell code runs, so YAML resource values should be used for runtime configuration/checking or for generated `qsub -l` commands, not assumed to rewrite the header dynamically.
- Activate the required venv before PBS-side YAML parsing so the script uses the venv's PyYAML instead of depending on packages installed in the module Python.
- For server setup docs, include a `bash -n` PBS syntax check and config-loading smoke test so users can validate the submission script without launching a full training job.

## 2026-06-30

- When moving repository lexicons, update `path.lexicon_path` in every preprocess config so synthesis and generation continue to load pronunciations.
- When moving the speech component packages, check both import statements and filesystem fallback paths such as the repo-local HiFi-GAN asset directory.
