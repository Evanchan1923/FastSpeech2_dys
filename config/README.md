# Config

This repo is configured for per-speaker SAPC dysarthric FastSpeech2 training.
Set the speaker in `SAPC_subset001/fastSpeech2_v1.yaml`, then submit
`qsub fastSpeech2_v1.pbs`.

## Active Config

- `SAPC_subset001/fastSpeech2_v1.yaml`: one combined SAPC config with these sections:
  - `resources`: runtime CPU and GPU settings read by the training script.
  - `run`: speaker, stage toggles, pretrained checkpoint, generation restore step, and MFA settings.
  - `preprocess`: HuggingFace SAPC input path, FastSpeech2 raw/preprocessed paths, and text/audio preprocessing.
  - `train`: optimizer, logging cadence, DataLoader settings, and output paths.
  - `gen`: SAPC dev split generation settings, including sample count and output subfolder.
  - `model`: FastSpeech2 model and HiFi-GAN vocoder settings.

The model config uses `multi_speaker: False`, so each run trains/fine-tunes one
speaker only.

## Server Paths

- Model/vocoder assets: `/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model`
- Training outputs: `/srv/scratch/speechdata/jinghao/fastSpeech2_result`
- Training data/intermediate files: `/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_fastSpeech2TTS`

The PBS script reads paths and runtime settings from `fastSpeech2_v1.yaml`.
Keep `resources.ncpu` and `resources.ngpu` matched with the PBS resource request
declared in `fastSpeech2_v1.pbs`.

Use `train.step.report_step` to control how often training loss is printed and
written to TensorBoard.
