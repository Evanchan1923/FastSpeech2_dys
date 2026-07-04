# FastSpeech2 SAPC Pipeline Summary

This repo trains and evaluates a FastSpeech2 text-to-speech model for the SAPC
dysarthric HuggingFace dataset.

## What The Model Does

At inference time, the TTS system takes text and produces audio:

```text
text -> phonemes -> FastSpeech2 mel-spectrogram -> HiFi-GAN waveform
```

FastSpeech2 itself predicts a mel-spectrogram. HiFi-GAN is the vocoder that turns
that mel-spectrogram into a `.wav` waveform.

The current config is per-speaker:

```yaml
multi_speaker: False
```

Each run is for one speaker. The HuggingFace rows are filtered to that speaker
before raw audio conversion, preprocessing, training, and dev-set generation.

In the current workflow, set the speaker once in:

```yaml
config/SAPC_subset001/fastSpeech2_v1.yaml
run:
  speaker: "<speaker_id>"
```

Then submit:

```bash
qsub fastSpeech2_v1.pbs
```

## Current Server Layout

Model/vocoder assets:

```text
/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model
```

Training outputs:

```text
/srv/scratch/speechdata/jinghao/fastSpeech2_result
```

Training/intermediate data:

```text
/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_fastSpeech2TTS
```

Active configs:

```text
config/SAPC_subset001/fastSpeech2_v1.yaml
```

The combined config contains `run`, `resources`, `preprocess`, `model`, `train`,
and `gen` sections.

## Pipeline Stages

### 1. Convert HuggingFace Rows To FastSpeech2 Raw Format

Enabled by `run.stages.prepare_align: True`.

Input:

```text
/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_subset/SPAC_subset001/train
```

Output:

```text
SAPC_fastSpeech2TTS/raw_data/SPAC_subset001/<speaker>/<utterance>.wav
SAPC_fastSpeech2TTS/raw_data/SPAC_subset001/<speaker>/<utterance>.lab
```

The SAPC adapter does not use torchcodec. It reads audio from HuggingFace
`bytes`, `array`, or `path` fields using `soundfile`, and uses `librosa` only for
resampling.

### 2. Forced Alignment

Enabled by `run.stages.mfa: True`.

MFA aligns `.wav` and `.lab` files and writes TextGrid alignments:

```text
SAPC_fastSpeech2TTS/preprocessed_data/SPAC_subset001/TextGrid/<speaker>/<utterance>.TextGrid
```

FastSpeech2 needs these alignments to learn duration prediction.

### 3. Acoustic Preprocessing

`utils/server-based/preprocess.py` reads raw audio plus TextGrid alignments and writes:

```text
mel/*.npy
pitch/*.npy
energy/*.npy
duration/*.npy
train.txt
val.txt
speakers.json
stats.json
```

These files live under:

```text
SAPC_fastSpeech2TTS/preprocessed_data/SPAC_subset001
```

### 4. Train FastSpeech2

Enabled by `run.stages.train: True`.

Outputs:

```text
/srv/scratch/speechdata/jinghao/fastSpeech2_result/output/ckpt/SPAC_subset001
/srv/scratch/speechdata/jinghao/fastSpeech2_result/output/log/SPAC_subset001
/srv/scratch/speechdata/jinghao/fastSpeech2_result/output/result/SPAC_subset001
```

Training uses automatic resume by default:

```yaml
run:
  training:
    restore_step: "latest"
```

With `restore_step: "latest"`, the job resumes the newest checkpoint if one is
present. If the checkpoint directory is empty, it starts at step 0 and can still
initialize from `pretrained_checkpoint`.

Fine-tune from an English pretrained checkpoint by setting:

```yaml
run:
  training:
    restore_step: "latest"
    pretrained_checkpoint: "/srv/scratch/speechdata/jinghao/fastSpeech2_tts_model/pretrained/LJSpeech/900000.pth.tar"
```

CPU/GPU runtime settings used by the training script are in the `resources`
section of:

```yaml
config/SAPC_subset001/fastSpeech2_v1.yaml
```

The training script uses PyTorch DataParallel when more than one visible GPU is
requested. The actual scheduler resource request remains in `fastSpeech2_v1.pbs`.

## Generation Check

After training, generate fixed dev-set samples by setting:

```yaml
run:
  stages:
    generate: True
```

By default this reads:

```text
/srv/scratch/speechdata/speech-corpora/dysarthric/SAPC_HF/SAPC_subset/SPAC_subset001/dev
```

and generates `100` samples. Tune this in:

```yaml
config/SAPC_subset001/fastSpeech2_v1.yaml
gen:
  generation:
    sample_count: 100
```

Outputs:

```text
/srv/scratch/speechdata/jinghao/fastSpeech2_result/output/result/SPAC_subset001/dev_samples/step_<restore_step>
```

The generation folder contains synthesized `.wav`, mel `.png`, and
`manifest.json`.

## Is This Training Or Fine-Tuning?

With the current code, this is training FastSpeech2 on one SAPC speaker from
scratch unless `run.training.pretrained_checkpoint` is set in `fastSpeech2_v1.yaml`.

Strictly speaking:

- Training from scratch: `run.training.restore_step: 0` and no pretrained checkpoint
- Continuing/resuming same run: `run.training.restore_step: <checkpoint_step>`
- Auto-resume same run: `run.training.restore_step: "latest"`
- Fine-tuning: initialize from a checkpoint trained on another dataset or a
  broader model, then continue training on one SAPC speaker

The original FastSpeech2 repo links pretrained checkpoints here:

```text
https://drive.google.com/drive/folders/1DOhZGlTLMbbAAFZmZGDdc77kz1PloS7F?usp=sharing
```

For this per-speaker English dysarthric setup, the best first checkpoint from
that folder is the English LJSpeech checkpoint. It is single-speaker and matches
the current `multi_speaker: False` model shape better than the LibriTTS
multi-speaker checkpoint.

## Mixed Speakers Vs Per-Speaker Models

The current config uses one multi-speaker model for all training speakers. This
is usually the better first experiment for SAPC if each speaker has limited data.

### Mixed-Speaker Multi-Speaker Model

Pros:

- More total training data, which usually improves pronunciation, duration, and
  general acoustic robustness.
- Better if each speaker has limited minutes of speech.
- The model learns shared dysarthric speech patterns while using speaker IDs to
  separate speaker identity.

Cons:

- If speakers differ strongly in intelligibility, articulation, microphone
  conditions, or prosody, the model can average those patterns.
- Speaker identity may be weaker if some speakers have very little data.
- If the dev speaker was never seen in training, this current speaker-embedding
  setup cannot synthesize that speaker directly.

### Per-Speaker Model

Pros:

- Can better preserve one speaker's voice and speaking style when that speaker
  has enough clean data.
- Avoids averaging across different dysarthric patterns.

Cons:

- Needs enough data per speaker. With too little data, quality and stability
  usually drop.
- More models to train, tune, and evaluate.
- Harder to compare if each speaker model has different data volume.

## Practical Recommendation

Since the current decision is per-speaker fine-tuning, train one run per speaker.
Use the LJSpeech checkpoint as initialization if possible.

Then evaluate:

- overall intelligibility and naturalness
- per-speaker quality
- whether severe speakers are being over-smoothed toward mild speakers
- whether specific speakers dominate the generated style

If one speaker has enough data and the multi-speaker output for that speaker is
not good, train a per-speaker model or fine-tune from the multi-speaker checkpoint
for that speaker. For dysarthric TTS, that two-stage approach is often pragmatic:

```text
multi-speaker baseline -> inspect per-speaker samples -> optional per-speaker fine-tune
```

## Important Caveat

If the goal is to generate audio for unseen speakers, this FastSpeech2 setup is
not enough by itself. It uses a learned speaker embedding table, so it works best
for speakers present during training. Unseen-speaker TTS would need a speaker
encoder, adaptation data, or another conditioning strategy.
