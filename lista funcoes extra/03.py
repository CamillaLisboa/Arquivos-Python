def checkNum(entrada):
    if len(entrada) == 4 and entrada.isdigit():
        if len(set(entrada)) > 2:
            return True
    return False

def crescente(num):
    num = ''.join(sorted(num))
    return int(num)

def decrescente(num):
    num = ''.join(sorted(num, reverse=True))
    return int(num)

def kaprekar(entrada):
    c = crescente(entrada)
    d = decrescente(entrada)
    num = d-c
    return num

while True:
    entrada = input()
    validate = checkNum(entrada)
    if not validate:
        break

print(entrada)

while True:
    num = kaprekar(entrada)
    print(num)
    if num == 6174:
        break
    entrada = str(num)
    