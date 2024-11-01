L = []
while True:
    try:
      n = input()
      d = int(input()) 
      L.append(d)
    except EOFError:
        print(f'{sum(L)/len(L):.1f}')
        break
