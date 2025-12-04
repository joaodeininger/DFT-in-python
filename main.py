import numpy as np

dados = np.loadtxt("entrada.txt")
N = dados.size
X = np.zeros(N, dtype=complex)
tol = 1e-12

for k in range(N):
    for n in range(N):
        X[k] += dados[n] * np.exp(-1j * 2 * np.pi * n * k / N)

# a = np.exp(np.pi * 1j)
# b = np.round(a, decimals=10)
y = np.round(X, decimals=10)
print(y)
