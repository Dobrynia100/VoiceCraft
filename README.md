
## QuickStart Docker
```bash

# 1.Порт 443 должен быть открыт.
# 2. Склонировать репозиторий
git clone git@github.com:jasonppy/VoiceCraft.git
cd VoiceCraft

# 3. Предполагается что у вас докер с nvidia container container-toolkit (В windows он по умолчанию)
# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.13.5/install-guide.html
# sudo apt-get install -y nvidia-container-toolkit-base || yay -Syu nvidia-container-toolkit || echo etc...

# 4. Собрать картинку
docker build --tag "voicecraft" .

# 5. Запуск через существующий файл или docker start /jupyter
./start-jupyter.sh  # linux
start-jupyter.bat   # windows

# 7. Посмотреть логи и ссылки для захода в Jupyter notebook можно либо в Контейнере Docker Desktop или введя команду
docker logs jupyter
или http://127.0.0.1:8888/lab

# 8. Проверка обнаружения видеокарты
nvidia-smi

# 9. Теперь в браузере inference_tts.ipynb 

```


## Inference Examples
Checkout [`inference_speech_editing.ipynb`](./inference_speech_editing.ipynb) and [`inference_tts.ipynb`](./inference_tts.ipynb)

## Gradio
### Run in colab


### How to use it
1. (optionally) Select models
2. Load models
3. Transcribe
4. (optionally) Tweak some parameters
5. Run
6. (optionally) Rerun part-by-part in Long TTS mode

### Some features
Smart transcript: write only what you want to generate

TTS mode: Zero-shot TTS

Edit mode: Speech editing

Long TTS mode: Easy TTS on long texts



## License
The codebase is under CC BY-NC-SA 4.0 ([LICENSE-CODE](./LICENSE-CODE)), and the model weights are under Coqui Public Model License 1.0.0 ([LICENSE-MODEL](./LICENSE-MODEL)). Note that we use some of the code from other repository that are under different licenses: `./models/codebooks_patterns.py` is under MIT license; `./models/modules`, `./steps/optim.py`, `data/tokenizer.py` are under Apache License, Version 2.0; the phonemizer we used is under GNU 3.0 License.

## Acknowledgement
We thank Feiteng for his [VALL-E reproduction](https://github.com/lifeiteng/vall-e), and we thank audiocraft team for open-sourcing [encodec](https://github.com/facebookresearch/audiocraft).

## Citation
```
@article{peng2024voicecraft,
  author    = {Peng, Puyuan and Huang, Po-Yao and Mohamed, Abdelrahman and Harwath, David},
  title     = {VoiceCraft: Zero-Shot Speech Editing and Text-to-Speech in the Wild},
  journal   = {arXiv},
  year      = {2024},
}
```

## Disclaimer
Any organization or individual is prohibited from using any technology mentioned in this paper to generate or edit someone's speech without his/her consent, including but not limited to government leaders, political figures, and celebrities. If you do not comply with this item, you could be in violation of copyright laws.

