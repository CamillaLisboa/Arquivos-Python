from random import randint

def linha(linha, matriz):
    result = max(matriz[linha])
    return result      

def coluna(coluna, matriz):
    result = max(linha[coluna] for linha in matriz)
    return result


matriz = [[randint(1, 20) for j in range(10)] for i in range(10)]

entrada = input().upper()
a = entrada[0]
b = int(entrada[1:])
if a[0] == 'L':
    result = linha(b, matriz)
    print(result)
elif a[0] == 'C':
    result = coluna(b, matriz)
    print(result)
else:
    print('ENTRADA INVÁLIDA')