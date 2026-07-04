# Project Context

- This repository trains and evaluates FastSpeech2 text-to-speech for the SAPC dysarthric HuggingFace dataset.
- The inference pipeline is `text -> phonemes -> FastSpeech2 mel-spectrogram -> HiFi-GAN waveform`.
- The active SAPC configs are `config/SAPC_subset001/fastSpeech2_v1.yaml` for per-speaker fine-tuning and `config/SAPC_subset001/fastSpeech2_v2.yaml` for selected-speaker multi-speaker training.
- `fastSpeech2_v1.yaml` is ordered for server editing: run paths/controls, dataset/output path-heavy sections, training runtime settings, then lower-touch model settings.
- SAPC runs set the target speaker in `config/SAPC_subset001/fastSpeech2_v1.yaml` using `run.speaker: "<speaker_id>"`, then submit with `qsub fastSpeech2_v1.pbs`.
- Multi-speaker SAPC runs use `fastSpeech2_v2.yaml` with `model.multi_speaker: True`, `run.speakers` reused as the train/dev speaker filter, shared multi-speaker paths, and submit with `qsub fastSpeech2_v2.pbs`.
- Current server paths are `/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model` for model/vocoder assets, `/srv/scratch/speechdata/jinghao/fastSpeech2_result` for training outputs, and `/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_fastSpeech2TTS` for training/intermediate data.
- Pipeline stages are prepare HuggingFace rows to FastSpeech2 raw `.wav`/`.lab`, run MFA for TextGrid alignments, preprocess acoustic features, train FastSpeech2, then generate dev-set samples.
- SAPC audio loading avoids torchcodec; the adapter reads HuggingFace `bytes`, `array`, or `path` fields with `soundfile` and uses `librosa` only for resampling.
- Training auto-resume is the default when `run.training.restore_step` is omitted. `"latest"` or `"auto"` picks the newest numeric checkpoint in the run checkpoint folder. If none exists, training starts at step 0 and uses `run.training.pretrained_checkpoint` when configured.
- Training from scratch still uses `training.restore_step: 0` with no pretrained checkpoint. Resuming can use a checkpoint step from the same run. Fine-tuning uses a checkpoint from another dataset or broader model, such as the LJSpeech checkpoint.
- Runtime CPU/GPU settings for the training script are stored as `train.resources.ncpu` and `train.resources.ngpu` in `config/SAPC_subset001/fastSpeech2_v1.yaml`; scheduler-only values such as select, memory, and walltime stay in `fastSpeech2_v1.pbs`.
- SAPC training reports losses at `step.report_step`, currently `5000`, while synthesis, validation, and save cadence remain controlled by their existing step settings.
- The pipeline summary is stored at `docs/PIPELINE_SUMMARY.md`.
- Repository lexicons are stored under `text/lexicon/`.
- Speech processing components are grouped under `speech/`: `speech/audio`, `speech/hifigan`, and `speech/preprocessor`.
- The config loader supports both legacy split YAML files and unified YAML files with named sections, so non-SAPC configs can remain split while SAPC uses one file.
