# Lessons Learned

## 2026-07-05

- On Katana, the conda-forge MFA install is the reliable path for `mfa version 3.3.9`; keep PBS conda activation and MFA preflight in sync.
- `mfa version` only confirms the MFA executable works; `mfa align` also needs the configured acoustic model downloaded, such as `mfa model download acoustic english_mfa`.
- MFA alignment can still fail after model download if `montreal-forced-aligner` and `kalpy` are version-incompatible; `TrainingGraphCompiler.__init__() got an unexpected keyword argument 'use_g2p'` points to that package mismatch.
- Pair MFA acoustic models with compatible MFA dictionaries, for example `english_mfa` with `english_us_mfa`, instead of using the repo Librispeech lexicon when MFA reports many dictionary phones missing from the acoustic model.
- Newer `librosa.resample` versions require keyword sample-rate arguments; use `orig_sr=` and `target_sr=` instead of positional sample rates.
- Keep `fastspeech2_v1.log` visible in git when debugging server PBS runs, because the user wants this diagnostic log included.

## 2026-07-03

- When consolidating YAML configs, add section extraction in the shared loader rather than teaching every caller a new file format.
- `librosa==0.9.2` imports `pkg_resources`, so the runtime Python environment needs a setuptools version that still provides it; pinning `setuptools==68.2.2` avoids missing `pkg_resources` failures.
- Python 3.10 cannot reliably install the original FastSpeech2-era pins such as `numpy==1.19.0`, `torch==1.7.0`, `librosa==0.7.2`, and `PyYAML==5.4.1`; keep `requirements.txt` aligned with the Python module loaded by PBS.
- For fine-tuning configs that keep `pretrained_checkpoint` set, auto-resume must still prefer the run checkpoint and restore optimizer state, otherwise resumed jobs silently lose optimizer history.
- PBS `#PBS` directives are parsed before shell code runs, so YAML resource values should be used for runtime configuration/checking or for generated `qsub -l` commands, not assumed to rewrite the header dynamically.
- Activate the required Python environment before PBS-side YAML parsing so the script uses that environment's PyYAML instead of depending on packages installed in the module Python.
- For server setup docs, include a `bash -n` PBS syntax check and config-loading smoke test so users can validate the submission script without launching a full training job.

## 2026-06-30

- When moving repository lexicons, update `path.lexicon_path` in every preprocess config so synthesis and generation continue to load pronunciations.
- When moving the speech component packages, check both import statements and filesystem fallback paths such as the repo-local HiFi-GAN asset directory.
