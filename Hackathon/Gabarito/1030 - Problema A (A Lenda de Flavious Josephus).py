def josephus(n, k):
    posicao_segura = 0
    for i in range(2, n + 1):
        posicao_segura = (posicao_segura + k) % i
    return posicao_segura + 1

nc = int(input())

for i in range(1, nc + 1):
    n, k = map(int, input().split())
    resultado = josephus(n, k)
    print(f"Case {i}: {resultado}")