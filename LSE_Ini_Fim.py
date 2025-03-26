class No:
    def __init__(self, val):
        self.info = val
        self.prox = None

    def getInfo(self):
        return self.info

    def getProx(self):
        return self.prox

    def setInfo(self, val):
        self.info = val

    def setProx(self, prox):
        self.prox = prox


class LSE2:
    def __init__(self):
        self.Inicio = None
        self.Fim = None

    def Ins_Inicio(self,val):
        p = No(val)
        if self.Inicio==None:  #lista esta vazia
            self.Inicio = p
            self.Fim = p
        else:
            p.setProx(self.Inicio)
            self.Inicio = p

    def Ins_Fim(self, val):
        p = No(val)
        if self.Inicio == None:  # lista esta vazia
            self.Inicio = p
            self.Fim = p
        else:
            self.Fim.setProx(p)
            self.Fim = p

    def Imprime(self):
        p = self.Inicio
        while p != None:
            print(p.getInfo(),"-->", end='')
            p = p.getProx()

        print("None")

    def Rem_Inicio(self):
        if self.Inicio==self.Fim: #existe 1 nó
            self.Inicio = None
            self.Fim = None
        else:
            self.Inicio = self.Inicio.getProx()

    def Rem_Fim(self):
        if self.Inicio==self.Fim: #existe 1 nó
            self.Inicio = None
            self.Fim = None
        else:
            p = self.Inicio
            #posicionando p no penúltimo nó da lista
            while (p.getProx() != self.Fim):
                p = p.getProx()

            p.setProx(None)
            self.Fim = p

    def Consulta(self, val):
        p = self.Inicio
        while (p != None and p.getInfo() != val):
            p = p.getProx()

        return p

    def Trans_Inicio(self, r):
        p = self.Inicio
        while (p.getProx() != r):
            p = p.getProx()

        p.setProx(r.getProx())
        r.setProx(self.Inicio)
        self.Inicio = r
        if r==self.Fim:
            self.Fim = p



L = LSE2()
while True:
    print("1 - Inserir no Inicio")
    print("2 - Inserir no Fim")
    print("3 - Imprimir a Lista")
    print("4 - Remover no Inicio")
    print("5 - Remover no Fim")
    print("6 - Consultar um Valor")

    print("7 - Transferir um Valor para o Inicio")

    print("0 - Sair do Programa")

    op = int(input("Digite a opcao: "))
    if op==0:
        break
    elif op==1:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Inicio(val)

    elif op == 2:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Fim(val)

    elif op==3:
        if L.Inicio==None:
            print("\nLista Vazia!")
        else:
            L.Imprime()

    elif op==4:
        if L.Inicio==None:
            print("\nLista Vazia!")
        else:
            L.Rem_Inicio()

    elif op==5:
        if L.Inicio==None:
            print("\nLista Vazia!")
        else:
            L.Rem_Fim()

    elif op==6:
        val = int(input("Digite o valor a procurar: "))
        r = L.Consulta(val)
        if r==None:
            print("\nValor nao existe na lista!")
        else:
            print("\nValor encontrado: ", r.getInfo())

    elif op==7:
        val = int(input("Digite o valor a transferir: "))
        r = L.Consulta(val)
        if r==None:
            print("\nValor nao existe na lista!")
        else:
            if r==L.Inicio:
                print("\nJá é o primeiro da lista!")
            else:
                L.Trans_Inicio(r)



