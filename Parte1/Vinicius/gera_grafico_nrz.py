from etapa3 import *

# Lista de valores de SNR para testar (ex.: de 5 a -40 dB)
snr_values = list(range(-20, -101, -1))

# Lista para armazenar quantidade de erros em cada SNR
errors = []

# Sinal limpo gerado a partir dos bits originais
clean_signal = encode_nrz(original_bits)

def contar_erros(original, decodificado):
    return sum(1 for a, b in zip(original, decodificado) if a != b)

print("Testando SNRs...")

for snr in snr_values:
    # Aplica ruído
    noisy = adicionar_ruido(clean_signal, snr)

    # Decodifica
    decoded = decode_nrz(noisy, len(original_bits))

    # Conta erros
    err = contar_erros(original_bits, decoded)
    errors.append(err)

    print(f"SNR = {snr:>3} dB  ->  Erros: {err}")

# --------- GERAR GRÁFICO ---------
import matplotlib.pyplot as plt

plt.figure(figsize=(9,5))
plt.plot(snr_values, errors, marker='o')
plt.xlabel("SNR (dB)")
plt.ylabel("Número de bits incorretos")
plt.title("Erros de bits por SNR")
plt.grid(True)
plt.savefig("grafico_erros_snr.png", dpi=300)

