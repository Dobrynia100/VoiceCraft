## VoiceCraft: Zero-Shot Speech Editing and Text-to-Speech in the Wild
VoiceCraft is a token infilling neural codec language model, that achieves state-of-the-art performance on both speech editing and zero-shot text-to-speech (TTS) on in-the-wild data including audiobooks, internet videos, and podcasts.

To clone or edit an unseen voice, VoiceCraft needs only a few seconds of reference.
## QuickStart Docker
```bash

# 1.Порт 443 должен быть открыт.

# 2. Склонировать репозиторий (например так) или любым другим методом
git clone git@github.com:jasonppy/VoiceCraft.git
cd VoiceCraft (или ваше название папки репозитория)

# 3. Предполагается что у вас докер с nvidia container container-toolkit (В windows он по умолчанию)
# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.13.5/install-guide.html
# sudo apt-get install -y nvidia-container-toolkit-base || yay -Syu nvidia-container-toolkit || echo etc...

# 4. Собрать картинку (c . в конце, ЭТО ВАЖНО !!!)
docker build --tag "voicecraft" . 

# 5. Запуск через существующий файл или docker start /jupyter
./start-jupyter.sh  # linux
start-jupyter.bat   # windows

# 6. Посмотреть логи и ссылки для входа в Jupyter notebook можно либо в Контейнере Docker Desktop или введя команду
docker logs jupyter

ссылка для доступа http://127.0.0.1:8888/lab

# 7. Проверка обнаружения видеокарты в консоли (не обязательно)
nvidia-smi

# 8. Теперь в юпитере запустить inference_tts.ipynb, не забудте поменять ядро на voicecraft (Также внутри будет скачиваться сама модель)

```

### Как использовать
1. (Опционально) Выбрать модель
2. Загрузить модель
3. Транскрипция аудио
4. (Опционально) поменять параметры
5. Запуск
6. (optionally) Rerun part-by-part in Long TTS mode

### Некоторые особенности
Транскрипция только того что нужно сгенерировать

Текст в речь

Режим редактирования речи




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

