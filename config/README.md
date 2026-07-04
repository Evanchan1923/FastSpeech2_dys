# Config

This repo has SAPC dysarthric FastSpeech2 configs for per-speaker fine-tuning
and true multi-speaker training.

## Active Config

- `SAPC_subset001/fastSpeech2_v1.yaml`: one combined SAPC config with these sections:
  - `run`: speaker, stage toggles, pretrained checkpoint, generation restore step, and MFA settings.
  - `preprocess`: HuggingFace SAPC input path, FastSpeech2 raw/preprocessed paths, and text/audio preprocessing.
  - `train`: runtime CPU/GPU settings, optimizer, logging cadence, DataLoader settings, and output paths.
  - `gen`: SAPC dev split generation settings, including sample count and output subfolder.
  - `model`: FastSpeech2 model and HiFi-GAN vocoder settings.
- `SAPC_subset001/fastSpeech2_v2.yaml`: selected-speaker multi-speaker SAPC
  config. It uses `model.multi_speaker: True`, filters train/dev rows through
  `run.speakers`, and writes to shared multi-speaker output folders.

Use `qsub fastSpeech2_v1.pbs` for per-speaker fine-tuning and
`qsub fastSpeech2_v2.pbs` for multi-speaker training.

## Server Paths

- Model/vocoder assets: `/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model`
- Training outputs: `/srv/scratch/speechdata/jinghao/fastSpeech2_result`
- Training data/intermediate files: `/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_fastSpeech2TTS`

The PBS scripts read paths and runtime settings from their matching YAML files.
Keep `train.resources.ncpu` and `train.resources.ngpu` matched with the PBS
resource request declared in the matching PBS file.

Use `train.step.report_step` to control how often training loss is printed and
written to TensorBoard.
