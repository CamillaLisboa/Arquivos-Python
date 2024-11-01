def Comb(n,k):
    if k == 1:
        return n
    if k == n:
        return 1
    return Comb(n-1, k-1) + Comb(n-1,k)

n,k = map(int, input().split())

print(f'Comb({n},{k}) = {Comb(n,k)}')