def maior(a, b):
    if a > b:
        return a
    return b

a,b = map(int,input().split())

print('O maior é',maior(a,b))