while True:
    try:
        h, m = map(int, input().split())
        print(f'{h//30:02}:{m//6:02}')
    except EOFError:
        break