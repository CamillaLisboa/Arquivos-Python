from random import randint
def procura(L,v):
    if L[0] == v:
        return True
    if len(L) ==1:
        return False
    return procura(L[1:], v)

lista = [randint(1,50) for i in range(10)]

valor = int(input())

pertence = procura(lista, valor)

if pertence:
    print(f'{valor} pertence a lista')
else:
    print(f'{valor} não pertence a lista')