def Ins_Fila(Fila, val):
    global first_senha, id_comum, senha_C, senha_P

    if first_senha:
        if val == 'P':
            Fila.append(senha_P)
            senha_P +=1
        if val == 'C':
            Fila.append(senha_C)
            senha_C += 1
        first_senha = False
    else:
        if val == 'P':
            if id_comum == 0:
                Fila.append(senha_P)
                senha_P +=1
            else:
                Fila.insert(id_comum, senha_P)
                senha_P +=1
                id_comum +=1
        if val ==  'C':
            Fila.append(senha_C)
            if id_comum == 0:
                id_comum = Fila.index(senha_C)
            senha_C += 1
            
            

def Imprime(Fila):
    for i in range(len(Fila)):
        print(Fila[i])


Fila=[]
first_senha = True
id_comum = 0
senha_C = 1000
senha_P = 2000

while True:
    print("1 - Inserir na Fila")
    print("3 - Imprimir a Fila")
    print("0 - Sair do Programa")

    op = int(input("Digite a opcao:"))
    if op==0:
        break

    elif op==1:
        val = input("Insira P para Prioridade e C para Comum: ").upper()
        Ins_Fila(Fila, val)
    
    elif op==3:
        if len(Fila) == 0:
            print("Fila Vazia!\n")
        else:
            print("\nFila:")
            Imprime(Fila)
