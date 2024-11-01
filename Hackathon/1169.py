n = int(input())
for i in range(n):
    t = int(input())
    cont = 1
    for j in range (t):
        cont*=2
    print(f'{cont//12//1000} kg')
