# funcao dft da numpy usada para confirmar os dados obtidos na nossa dft

import numpy as np

dados = np.loadtxt("entrada.txt")

# --- O CÁLCULO DA DFT ---
# Em vez dos loops manuais, usamos isso:
X = np.fft.fft(dados)

# Opcional: Calcular as frequências correspondentes ao eixo X
# Isso gera o vetor de frequências (0, 1, ..., N/2, -N/2, ..., -1)
freqs = np.fft.fftfreq(dados.size)

print(X)
