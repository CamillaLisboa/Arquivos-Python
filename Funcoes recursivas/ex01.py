def potencia(base, expo):
    if expo == 0:
        return 1
    return base *potencia(base, expo-1)

a,b = map(int, input().split())

print(f' {a} elevado a {b} = {potencia(a,b)}')