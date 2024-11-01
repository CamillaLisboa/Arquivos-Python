from math import factorial as fat
n= int(input())

for i in range(n):
    p,s = map(int, input().split())
    p=str(fat(p)).split()
    for j in range(p):
        if len(p) > 1:
            p.remove(p[j+s])
    print(f'Case {i}: {p[0]}')