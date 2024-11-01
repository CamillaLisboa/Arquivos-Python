def verificar_dieta(dieta, cafe_manha, almoco):
    consumido = cafe_manha + almoco
    dieta_set = set(dieta)
    consumido_set = set(consumido)
    if not consumido_set.issubset(dieta_set):
        return "CHEATER"
    for alimento in consumido:
        if consumido.count(alimento) > dieta.count(alimento):
            return "CHEATER"
    restante = sorted(dieta_set - consumido_set)
    return "".join(restante)

n = int(input())

for i in range(n):
    dieta = input().strip()
    cafe_manha = input().strip()
    almoco = input().strip()

    resultado = verificar_dieta(dieta, cafe_manha, almoco)
    print(resultado)

