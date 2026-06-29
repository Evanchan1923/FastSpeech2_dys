# Config

This repo is configured for per-speaker SAPC dysarthric FastSpeech2 training.
Set the speaker in `SAPC_subset001/run.yaml`, then submit `qsub fastSpeech2_v1.pbs`.

## Active Config

- `SAPC_subset001/preprocess.yaml`: HuggingFace SAPC input path, FastSpeech2 raw/preprocessed paths, text/audio preprocessing.
- `SAPC_subset001/model.yaml`: FastSpeech2 model and HiFi-GAN vocoder settings.
- `SAPC_subset001/train.yaml`: optimizer settings and output paths.
- `SAPC_subset001/gen.yaml`: SAPC dev split generation settings, including sample count and output subfolder.
- `SAPC_subset001/run.yaml`: speaker, stage toggles, pretrained checkpoint, and MFA settings.

The model config uses `multi_speaker: False`, so each run trains/fine-tunes one
speaker only.

## Server Paths

- Model/vocoder assets: `/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model`
- Training outputs: `/srv/scratch/speechdata/jinghao/fastSpeech2_result`
- Training data/intermediate files: `/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_fastSpeech2TTS`

The PBS script reads these paths from the YAML files at runtime.
