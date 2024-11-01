import sys
sys.setrecursionlimit(1000000)

def dfs(i, j, matriz, dp, N, M):
    if dp[i][j] != -1:
        return dp[i][j]

    max_power = matriz[i][j]
    
    # Direções: cima, baixo, esquerda, direita
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for di, dj in direcoes:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and matriz[ni][nj] <= max_power:
            max_power = max(max_power, matriz[i][j] + dfs(ni, nj, matriz, dp, N, M))
    
    dp[i][j] = max_power
    return dp[i][j]

def calcular_poder_maximo(matriz, N, M):
    dp = [[-1] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if dp[i][j] == -1:
                dfs(i, j, matriz, dp, N, M)
    
    return dp

# Leitura da entrada
N, M = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(N)]

# Calcula o poder máximo para cada célula
resultado = calcular_poder_maximo(matriz, N, M)

# Imprime o resultado
for linha in resultado:
    print(" ".join(map(str, linha)))
