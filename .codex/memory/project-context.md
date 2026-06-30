# Project Context

- This repository trains and evaluates FastSpeech2 text-to-speech for the SAPC dysarthric HuggingFace dataset.
- The inference pipeline is `text -> phonemes -> FastSpeech2 mel-spectrogram -> HiFi-GAN waveform`.
- The active SAPC configs live under `config/SAPC_subset001/`: `preprocess.yaml`, `model.yaml`, `train.yaml`, `gen.yaml`, and `run.yaml`.
- SAPC runs set the target speaker in `config/SAPC_subset001/run.yaml` using `speaker: "<speaker_id>"`, then submit with `qsub fastSpeech2_v1.pbs`.
- Current server paths are `/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model` for model/vocoder assets, `/srv/scratch/speechdata/jinghao/fastSpeech2_result` for training outputs, and `/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_fastSpeech2TTS` for training/intermediate data.
- Pipeline stages are prepare HuggingFace rows to FastSpeech2 raw `.wav`/`.lab`, run MFA for TextGrid alignments, preprocess acoustic features, train FastSpeech2, then generate dev-set samples.
- SAPC audio loading avoids torchcodec; the adapter reads HuggingFace `bytes`, `array`, or `path` fields with `soundfile` and uses `librosa` only for resampling.
- Training from scratch uses `training.restore_step: 0` with no pretrained checkpoint. Resuming uses a checkpoint step from the same run. Fine-tuning uses a checkpoint from another dataset or broader model, such as the LJSpeech checkpoint.
- The pipeline summary is stored at `docs/PIPELINE_SUMMARY.md`.
- Repository lexicons are stored under `text/lexicon/`.
- Speech processing components are grouped under `speech/`: `speech/audio`, `speech/hifigan`, and `speech/preprocessor`.
