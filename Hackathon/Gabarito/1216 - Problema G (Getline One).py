soma_distancias = 0
quantidade_amigos = 0
while True:
    try:
        nome = input()
        distancia = int(input())
        soma_distancias += distancia
        quantidade_amigos += 1
    except EOFError:
        break
media_distancias = soma_distancias / quantidade_amigos
print(f"{media_distancias:.1f}")
