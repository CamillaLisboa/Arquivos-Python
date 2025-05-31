def Ins_Fila(Fila, val):
    global senha_C, senha_P, id_comum

    if val == 'P':
        if id_comum == -1:
            Fila.append(senha_P)
        else:
            Fila.insert(id_comum, senha_P)
            id_comum += 1  
        senha_P += 1

    elif val == 'C':
        Fila.append(senha_C)
        if id_comum == -1:
            id_comum = len(Fila) - 1 
        senha_C += 1
            
def ChamarSenha(Fila):
    global id_comum
    senha = Fila.pop(0)

    if 2000 <= senha:
        print(f"Senha: P-{senha}")
        if id_comum > 0:
            id_comum -= 1  
    else:
        print(f"Senha: C-{senha}")
        if id_comum > 0:
            id_comum -= 1
        elif not any(1000 <= s < 2000 for s in Fila):  
            id_comum = -1       

def Imprime(Fila):
    for senha in Fila:
        prefixo = 'P' if senha >= 2000 else 'C'
        print(f"{prefixo}-{senha}")


Fila=[]
id_comum = -1
senha_C = 1000
senha_P = 2000

while True:
    print("1 - Retirar Senha")
    print("2 - Chamar Senha")
    print("3 - Imprimir a Fila")
    print("0 - Encerrar Chamada de Senha")

    op = int(input("Digite a opcao:"))
    if op==0:
        if len(Fila) > 0:
            print("Ainda há senhas para serem chamadas")
        else:
            break

    elif op==1:
        val = input("Informe P para Prioridade e C para Comum: ").upper()
        Ins_Fila(Fila, val)

    elif op==2:
        ChamarSenha(Fila)
    
    elif op==3:
        if len(Fila) == 0:
            print("Fila Vazia!\n")
        else:
            print("\nFila:")
            Imprime(Fila)
