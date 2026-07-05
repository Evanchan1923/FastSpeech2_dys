# FastSpeech2 SAPC TTS

This repo is the code/config/PBS submission package for training FastSpeech2 on the
SAPC dysarthric HuggingFace dataset.

For the end-to-end pipeline explanation and speaker-mixing guidance, see
`docs/PIPELINE_SUMMARY.md`.

## Server Layout

- Model/vocoder assets: `/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model`
- Training outputs: `/srv/scratch/speechdata/jinghao/fastSpeech2_result`
- Training data/intermediate files: `/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_fastSpeech2TTS`
- Input HuggingFace split: `/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_subset/SPAC_subset001/train`

## Model Assets

HiFi-GAN assets are stored on the server under:

```text
/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model
```

Expected layout:

```text
/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model/hifigan/config.json
/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model/hifigan/generator_universal.pth.tar.zip
```

The HiFi-GAN checkpoint may remain zipped. The code extracts the needed checkpoint
automatically on first use if the `.pth.tar` file is not already present.

## Training Job

For per-speaker fine-tuning, edit `config/SAPC_subset001/fastSpeech2_v1.yaml` and set:

```yaml
run:
  speaker: "<speaker_id>"
```

Then submit:

```bash
qsub fastSpeech2_v1.pbs
```

For true multi-speaker training across a selected speaker subset, edit
`run.speakers` in `config/SAPC_subset001/fastSpeech2_v2.yaml`, then use:

```bash
qsub fastSpeech2_v2.pbs
```

The v2 config uses `model.multi_speaker: True`, reuses `run.speakers` for train
and generation filtering, and writes to shared multi-speaker folders.

The PBS script reads stage controls from the `run` section:

```yaml
run:
  stages:
    prepare_align: True
    mfa: True
    preprocess: True
    train: True
    generate: True
```

Training defaults to automatic resume. The job resumes the newest checkpoint in
the run checkpoint folder. If no checkpoint exists, it starts at step 0 and uses
`pretrained_checkpoint` as initialization when that path is set. Set
`run.training.restore_step` only when you want to force a specific checkpoint or
force scratch training with `0`.

Runtime CPU/GPU settings live in `train.resources`. The scheduler request itself
stays in `fastSpeech2_v1.pbs`.

Training loss/report cadence is controlled by `train.step.report_step`; the SAPC
default is `5000`.

For conda environment setup and a copy-paste PBS smoke test, see
`docs/PBS_CONDA_SETUP.md`.

## Per-Speaker Fine-Tuning

The SAPC config is set up for per-speaker fine-tuning. The speaker is selected
with `config/SAPC_subset001/fastSpeech2_v1.yaml`, and each speaker gets separate
raw, preprocessed, checkpoint, log, and generated-result folders.

The original FastSpeech2 repo provides pretrained checkpoints here:

```text
https://drive.google.com/drive/folders/1DOhZGlTLMbbAAFZmZGDdc77kz1PloS7F?usp=sharing
```

For English per-speaker fine-tuning, use the LJSpeech checkpoint as the first
choice because it is an English single-speaker FastSpeech2 checkpoint and matches
the current `multi_speaker: False` config.

Suggested server location:

```text
/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model/pretrained/LJSpeech/900000.pth.tar
```

Fine-tune from that checkpoint by setting:

```yaml
run:
  training:
    pretrained_checkpoint: "/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model/pretrained/LJSpeech/900000.pth.tar"
```

## Generation Check

After training, generate fixed SAPC dev samples by keeping this enabled in
`fastSpeech2_v1.yaml`:

```yaml
run:
  stages:
    generate: True
```

By default this uses the latest checkpoint and generates `100` samples from:

```text
/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_subset/SPAC_subset001/dev
```

Outputs are written under the training result directory:

```text
/srv/scratch/speechdata/jinghao/fastSpeech2_result/output/result/SPAC_subset001/dev_samples/step_<restore_step>
```

Tune generation in the `gen` section of:

```text
config/SAPC_subset001/fastSpeech2_v1.yaml
```

## Active Config

```text
config/SAPC_subset001/fastSpeech2_v1.yaml
```

The SAPC adapter reads HuggingFace rows and writes FastSpeech2 raw `.wav`/`.lab`
files without torchcodec. It decodes audio bytes/path/array using `soundfile` and
uses `librosa` only for resampling.
