T = int(input())
for i in range(T):
    n = input().split()
    m = n[1::]
    m.sort()
    print(f'Case {i+1}: {m[int(n[0])//2]}')
