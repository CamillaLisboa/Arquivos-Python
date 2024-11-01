import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())

for i in range(1, N + 1):
    S1 = input().strip()
    S2 = input().strip()

    num1 = int(S1, 2)
    num2 = int(S2, 2)

    if gcd(num1, num2) > 1:
       print(f"Pair #{i}: All you need is love!")
    else:
       print(f"Pair #{i}: Love is not all you need!")
