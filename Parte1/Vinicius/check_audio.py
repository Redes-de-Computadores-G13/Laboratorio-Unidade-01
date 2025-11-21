import sounddevice as sd
import soundfile as sf
from modularizacao import *

audio, sr = sf.read("dados_codificados/dados_123110505_44100hz.wav")

samples_per_bit = int(sr * BIT_DURATION)

# Tocar os primeiros 5 bits
for i in range(31):
    start = i * samples_per_bit
    end = start + samples_per_bit
    bit_audio = audio[start:end]

    print(f"Bit {i} (tocado agora)")
    sd.play(bit_audio, sr)
    sd.wait()  # Espera terminar antes de tocar o próximo

