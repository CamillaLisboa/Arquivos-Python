T = int(input())

for i in range(1, T + 1):
    entrada = list(map(int, input().split()))
    N = entrada[0]  
    idades = entrada[1:]  
    idade_capitao = idades[N // 2]
    print(f"Case {i}: {idade_capitao}")
