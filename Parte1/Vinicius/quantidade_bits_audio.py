import soundfile as sf
from modularizacao import *

audio, sr = sf.read("dados_codificados/dados_123110505_44100hz.wav")
duration = len(audio) / sr

num_bits = int(duration / BIT_DURATION)
print(num_bits)

