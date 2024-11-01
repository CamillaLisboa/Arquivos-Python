def primo(num):
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True

def intervalo (ini, fim):
    primos=[]
    for i in range(ini, fim):
        prime = primo(i)
        if prime == True:
            primos.append(i)
    return primos

a,b = map(int,input().split()) 
print(intervalo(a,b))