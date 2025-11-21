from modularizacao import *

# Dados de teste
test_data = "1010100000001111110000010101010111000"

print(f"Criando arquivos de teste para: {test_data}")

# NRZ
nrz_signal = encode_nrz(test_data)
sf.write('teste_nrz.wav', nrz_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_nrz.wav criado")

# Manchester
manchester_signal = encode_manchester(test_data)
sf.write('teste_manchester.wav', manchester_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_manchester.wav criado")


original_data = test_data

print(f"\nDados originais: {original_data}")
print(f"Número de bits: {len(original_data)}\n")




# Testa decodificação NRZ
print("1. Decodificando NRZ:")
nrz_audio, _ = sf.read('teste_nrz.wav')
decoded_nrz = decode_nrz(nrz_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_nrz}")
print(f"Correto: {original_data == decoded_nrz}\n")




# Testa decodificação Manchester
print("3. Decodificando Manchester:")
manchester_audio, _ = sf.read('teste_manchester.wav')
decoded_manchester = decode_manchester(manchester_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_manchester}")
print(f"Correto: {original_data == decoded_manchester}")

print("\n--------------------------\n")

my_file = "dados_codificados/dados_123110505_44100hz.wav"
# Testa decodificação NRZ
print("1. Decodificando NRZ:")
nrz_audio_msg, _ = sf.read(my_file)
decoded_nrz_msg = decode_nrz(nrz_audio_msg, 31)
print(f"Decodificado: {decoded_nrz_msg}")
print(f"Número de bits: {len(decoded_nrz_msg)}")

# Testa decodificação Manchester
print("3. Decodificando Manchester:")
manchester_audio_msg, _ = sf.read(my_file)
decoded_manchester_msg = decode_manchester(manchester_audio_msg, 31)
print(f"Decodificado: {decoded_manchester_msg}")
print(f"Número de bits: {len(decoded_manchester_msg)}")
