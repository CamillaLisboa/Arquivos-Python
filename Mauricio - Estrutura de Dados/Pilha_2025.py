
def Push(Pilha, val):
    global topo
    topo += 1
    Pilha[topo]=val

def Pop(Pilha):
    global topo
    x = Pilha[topo]
    topo-=1
    return x

def Imprime(Pilha):
    global topo
    for i in range(topo, -1, -1):
        print("[", Pilha[i],"]")

def Converte (Pilha, val):
    while val>0:
        Push(Pilha, val % 2)
        val //= 2

    global topo
    bin=0
    while topo>=0:
        x = Pop(Pilha)
        bin = bin*10+x

    return bin


Pilha=[0]*10
topo = -1   #Pilha está vazia
while True:
    print("\n1 - Inserir na Pilha")
    print("2 - Remover da Pilha")
    print("3 - Imprimir a Pilha")
    print("4 - Converter decimal para binario")
    print("0 - Sair do Programa")

    op = int(input("Digite a opcao: "))

    if op==0:
        break
    elif op==1:
        val = int(input("Digite o valor a inserir:"))
        if topo == len(Pilha)-1:
            print("\nPilha cheia!")
        else:
            Push(Pilha, val)
    elif op==2:
        if topo==-1:
            print("\nPilha vazia")
        else:
            val = Pop(Pilha)
            print("\nValor removido: ", val)
    elif op==3:
        if topo==-1:
            print("\nPilha vazia!")
        else:
            print("\nPilha:")
            Imprime(Pilha)
    elif op==4:
        val = int (input("Digite o valor em decimal:"))
        bin = Converte(Pilha, val)
        print("\nValor em binario:", bin)






