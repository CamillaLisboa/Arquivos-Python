def Push(Pilha, val):
    global topo
    topo += 1
    Pilha[topo]=val

def Pop(Pilha):
    global topo
    x = Pilha[topo]
    topo-=1
    return x

def Ordena(Pilha, val):
    global topo
    Aux = []

    while Pilha[topo] < val:
        x = Pop(Pilha)
        Aux.append(x)

        Push(Pilha,val)
        
        while len(Aux) > 0:
            x = Aux.pop()
            Push(Pilha, x)

    
def Imprime(Pilha):
    global topo
    for i in range(topo, -1, -1):
        print("[", Pilha[i],"]")

Pilha=[0]*10
topo = -1   #Pilha está vazia
while True:

    print("\n1 - Inserir valores")
    print("2 - Retirar valores")
    print("3 - Mostrar Pilha")
    print("0 - Sair do programa")

    op = int(input("Digite a opcao desejada:"))

    if op==0:
        break
    elif op==1:
        if topo == len(Pilha)-1:
                print("\nPilha cheia!")
        else:
            Push(Pilha, topo+1)
        
    elif op==2:
        x = Pop(Pilha)
        print(x)
    
    elif op==3:
        if topo==-1:
            print("\nPilha!")
        else:
            print("\nPilha:")
            Imprime(Pilha)
        