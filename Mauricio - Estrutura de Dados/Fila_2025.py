
def Ins_Fila(Fila, nome, id):
    x = [nome, id]
    Fila.append(x)

def Imprime(Fila):
    for i in range(len(Fila)):
        print(Fila[i][0],Fila[i][1])

def Primeiro (Fila):
    return Fila[0][0]

def Remove(Fila):
    Fila.pop(0)

def Trans_Idoso(Fila):
    idoso = max(Fila, key = lambda x:x[1])
    Fila.remove(idoso)
    Fila.insert(0, idoso)



Fila =[]
while True:
    print("1 - Inserir na Fila")
    print("2 - Retirar da Fila")
    print("3 - Imprimir a Fila")
    print("4 - Transferir Idoso para Inicio")
    print("0 - Sair do Programa")

    op = int(input("Digite a opcao:"))
    if op==0:
        break
    elif op==1:
        nome = input("Digite o nome da pessoa: ")
        id = int(input("Digite a idade da pessoa: "))
        Ins_Fila(Fila, nome, id)

    elif op==2:
        if len(Fila)==0:
            print("Fila Vazia!\n")
        else:
            nome = Primeiro(Fila)
            print("\nChamando: ", nome)
            Remove(Fila)
    elif op==3:
        if len(Fila) == 0:
            print("Fila Vazia!\n")
        else:
            print("\nFila:")
            Imprime(Fila)

    elif op==4:
        Trans_Idoso(Fila)

