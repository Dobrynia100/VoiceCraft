import librosa
import os
import numpy as np
from scipy.stats import pearsonr

def load_audio(file_path):
    y, sr = librosa.load(file_path, sr=None)
    return y, sr

def normalize_audio(y):
    return (y - np.mean(y)) / np.std(y)

def calculate_pearson_correlation(y1, y2):
    correlation, _ = pearsonr(y1, y2)
    return correlation

current_directory = os.getcwd()
files = os.listdir(current_directory)
audio_files = [file for file in files if file.endswith('.wav')]

if len(audio_files) < 2:
    print("Недостаточно аудиофайлов для сравнения.")
else:
    file_path1 = os.path.join(current_directory, audio_files[0])
    file_path2 = os.path.join(current_directory, audio_files[1])

    audio_data1 = load_audio(file_path1)
    audio_data2 = load_audio(file_path2)

y1, sr1 = load_audio(file_path1)
y1_normalized = normalize_audio(y1)

y2, sr2 = load_audio(file_path2)
y2_normalized = normalize_audio(y2)

if sr1 != sr2:
    raise ValueError("Аудиофайлы имеют разные частоты дискретизации")


min_length = min(len(y1_normalized), len(y2_normalized))
y1_normalized = y1_normalized[:min_length]
y2_normalized = y2_normalized[:min_length]

correlation = calculate_pearson_correlation(y1_normalized, y2_normalized)

print(f"Коэффициент корреляции Пирсона: {correlation}")
