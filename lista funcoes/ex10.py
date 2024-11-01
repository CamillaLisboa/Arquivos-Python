from math import sqrt

def calculaDelta(a,b,c):
    x = b**2- 4*a*c
    return x

def raizes(a,b,c):
    delta = calculaDelta(a,b,c)
    if delta< 0:
        return 'Não existe raíz'
    if delta == 0:
        x= -b /(2*4)
        return f'Raíz única: {x}'
    else:
        x1 = (-b + sqrt(delta)) / 2*a
        x2 = (-b - sqrt(delta)) / 2*a
        return f'Duas raizes reais: x1 = {x1} e x2 = {x2}'

a,b,c = map(int, input('Entre com as variáveis a, b e c').split())
print(raizes(a,b,c))