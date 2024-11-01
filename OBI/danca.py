def resolver(N, M, P, ordens):
    linhas = list(range(N))
    colunas = list(range(M))

    for ordem in ordens:
        tipo, A, B = ordem
        A -= 1
        B -= 1

        if tipo == 'L':
            linhas[A], linhas[B] = linhas[B], linhas[A]
        elif tipo == 'C':
            colunas[A], colunas[B] = colunas[B], colunas[A]

    for i in range(N):
        linha_atual = []
        for j in range(M):
            linha_atual.append(linhas[i] * M + colunas[j] + 1)
        print(" ".join(map(str, linha_atual)))

N, M, P = map(int, input().split())
ordens = [input().split() for _ in range(P)]

ordens = [(ordem[0], int(ordem[1]), int(ordem[2])) for ordem in ordens]

resolver(N, M, P, ordens)
