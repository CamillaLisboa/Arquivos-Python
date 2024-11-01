def mdc(x,y):
    if (x>= y) and (x % y == 0):
        return y
    if x<y:
        return mdc(y,x)
    return mdc(y, x%y)
    
x,y = map(int, input().split())
print(f'O MDC({x},{y}) = {mdc(x,y)}')