def movimentos_dama(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return 1
    else:
        return 2

while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    print(movimentos_dama(x1, y1, x2, y2))