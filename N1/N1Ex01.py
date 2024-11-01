def commonChar(a,b):
    comum=[]
    for char in a:
        if char in b:
            comum.append(char)
    return ''.join(comum)

a,b = input().split()
print(commonChar(a,b))