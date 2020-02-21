PyTorch implementation of
[Efficiently Trainable Text-to-Speech System Based on Deep Convolutional Networks with Guided Attention](https://arxiv.org/abs/1710.08969) based on the following projects:
* https://github.com/tugstugi/pytorch-dc-tts (majority code)
* https://github.com/Kyubyong/dc_tts (audio pre processing)
* https://github.com/r9y9/deepvoice3_pytorch (data loader sampler)

## Online Text-To-Speech Demo
The following notebooks are executable on [https://colab.research.google.com ](https://colab.research.google.com):
* [English Female Voice TTS Demo (LJ-Speech)](https://colab.research.google.com/github/tugstugi/pytorch-dc-tts/blob/master/notebooks/EnglishTTS.ipynb)

For audio samples and pretrained models, visit the above notebook links.

## Training/Synthesizing English Text-To-Speech
The English TTS uses the [LJ-Speech](https://keithito.com/LJ-Speech-Dataset/) dataset.
1. Download the dataset: `python dl_and_preprop_dataset.py --dataset=ljspeech`
2. Train the Text2Mel model: `python train-text2mel.py --dataset=ljspeech`
3. Train the SSRN model: `python train-ssrn.py --dataset=ljspeech`
4. Synthesize sentences: `python synthesize.py --dataset=ljspeech`
   * The WAV files are saved in the `samples` folder.
