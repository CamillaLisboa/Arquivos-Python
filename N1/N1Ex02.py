from random import sample

def newList(inf,sup,numbers):
    A=[]
    for num in numbers:
        if num >= inf and num <= sup:
            A.append(num)
    return A

numbers = sorted(sample(range(1, 51), 15))
inf,sup = map(int, input().split())
print(newList(inf,sup,numbers))
    