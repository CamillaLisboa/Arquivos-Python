def expoente (base, expoente):
    result=1
    for num in range (expoente):
        result*=base
    return result

a,b = map(int,input().split())
print(expoente(a,b))