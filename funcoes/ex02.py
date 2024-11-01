def ordem (a, b , c ):
    if a > b or a > c:
        if b < c:
            a,b = b,a
        else:
            a,c = c,a
    if b > c:
        b,c = c,b
        
    return a, b, c

a,b,c = map(int, input().split())
print(ordem(a,b,c))