def Push(Pilha, val):
    global topo
    topo += 1
    Pilha[topo]=val

def Pop(Est):
    global topo
    x = Est[topo]
    topo-=1
    return x

def Retira(Est, val):
    global topo
    Rua = []

    if Est[topo] == val:
        Pop(Est)
    else:
        while Est[topo] != val:
            x = Pop(Est)
            Rua.append(x)

        x = Pop(Est)
        
        while len(Rua) > 0:
            x = Rua.pop()
            Push(Est, x)

    
def Imprime(Pilha):
    global topo
    for i in range(topo, -1, -1):
        print("[", Pilha[i],"]")

Est=[0]*10
topo = -1   #Pilha está vazia
while True:

    print("\n1 - Estacionar")
    print("2 - Retirar veiculo")
    print("3 - Mostrar estacionamento")
    print("0 - Sair do programa")

    op = int(input("Digite a opcao desejada:"))

    if op==0:
        break
    elif op==1:
        if topo == len(Est)-1:
                print("\nPilha cheia!")
        else:
            Push(Est, topo+1)
        
    elif op==2:
        val = int(input("Digite o valor do carro a ser retirado:"))
        Retira(Est, val)
    
    elif op==3:
        if topo==-1:
            print("\nEstacionamento vazio!")
        else:
            print("\nEstacionamento:")
            Imprime(Est)
        