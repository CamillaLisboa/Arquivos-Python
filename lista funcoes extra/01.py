def getData(entrada):
    entrada = entrada.split()
    n = int(entrada[0])
    letra = entrada[1]
    return n, letra

def checkAlfabeto(letra):
    if letra == 'maiusculas':
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "abcdefghijklmnopqrstuvwxyz"

def creatPiramide(alfabeto,n):
    linhas=[]
    for i in range(1, n + 1):
        letras = alfabeto[:i]
        linhas.append('.' * (26 - i) + letras)
    return linhas

entrada = input().lower()
n, letra = getData(entrada)

alfabeto = checkAlfabeto(letra)
piramide = creatPiramide(alfabeto, n)

print('\n'.join([linha for linha in piramide]))

