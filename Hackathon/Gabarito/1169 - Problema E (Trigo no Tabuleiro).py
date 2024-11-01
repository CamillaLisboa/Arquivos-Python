def calcular_kg_trigo(X):
    total_graos = (2 ** X) - 1
    kg_trigo = total_graos // (12 * 1000)
    return kg_trigo


N = int(input())
for _ in range(N):
    X = int(input())
    resultado = calcular_kg_trigo(X)
    print(resultado, 'kg')
