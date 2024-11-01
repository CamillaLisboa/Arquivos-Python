def verify(K, N, alfa, msg):
    alfabeto_set = set(alfa)
    
    for char in msg:
        if char not in alfabeto_set:
            print("N")
            return

    print("S")

K, N = map(int, input().split())
alfa = input().strip()
msg = input().strip()

verify(K, N, alfa, msg)

