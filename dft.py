import time  # biblioteca para medir o tempo de execução do código

inicio = time.time()  # inicia o contador de tempo
import numpy as np  # biblioteca para manipular arrays e realizar operações matemáticas mais avançadas

dados = np.loadtxt("entrada.txt")  # carrega os dados do arquivo de entrada
N = dados.size  # tamanho da amostragem
X = np.zeros(
    N, dtype=complex
)  # array pre-carregado com zeros para inserir os dados posteriormente
tol = 1e-12  # valor de tolerância apenas usado para arredondar valores muito pequenos

for k in range(N):  # somatório de k
    for n in range(N):  # somatório de n
        X[k] += dados[n] * np.exp(-1j * 2 * np.pi * n * k / N)  # equação da DFT

# a = np.exp(np.pi * 1j)
# b = np.round(a, decimals=10)
y = np.round(
    X, decimals=10
)  # arredonda os valores de X(k) quando são muito pequenos (os valores sempre ficam com resíduos pois o pi do programa é finito)

np.savetxt("saida.txt", y)  # salva X(k) no arquivo saida.txt
print(y)

fim = time.time()  # fim do contador de tempo
print(
    "Tempo:", fim - inicio, "segundos"
)  # o tempo de execução é a diferença entre o tempo final e o inicial
