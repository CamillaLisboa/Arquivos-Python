while True:
    try:
        hashmat, oponente = map(int, input().split())
        diferenca = abs(hashmat - oponente)
        print(diferenca)
    except EOFError:
        break
