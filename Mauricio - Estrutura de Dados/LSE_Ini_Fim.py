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

    def Ins_Inicio(self, val):
        p = No(val)

        if self.Inicio == None:
            self.Inicio = p
            self.Fim = p
        else:
            p.setProx(self.Inicio)
            self.Inicio = p

    def Ins_Fim(self, val):
        p = No(val)
        
        if self.Inicio == None:
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
        p = self.Inicio
        
        if p.getProx() == None:
            self.Inicio = None
            self.Fim = None
        else:
            self.Inicio = p.getProx()

    def Rem_Meio(self,r):
        p=self.Inicio
        while p.getProx() != r:
            p=p.getProx()

        q= r.getProx()
        p.setProx(q)


    def Rem_Fim(self):
        p = self.Inicio

        while p.getProx() != self.Fim:
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

    def Trans_Final(self,r):
        p= self.Inicio
        
        if self.Inicio == r:
            self.Inicio = r.getProx()
        else:
            while p.getProx() != r:
                p=p.getProx()
            p.setProx(r.getProx())
        self.Fim.setProx(r)
        r.setProx(None)
        self.Fim = r

    def Rem_Oco(self):

        p = self.Inicio
        while p is not None:
            q = p.getProx()
            while q is not None:
                if p.getInfo() == q.getInfo():
                    if q == self.Fim:
                        self.Rem_Fim()
                    else:
                        self.Rem_Meio(q)
                    q = p.getProx()
                else:
                    q = q.getProx()
            p = p.getProx()
        print("Ocorrências removidas com sucesso, se existirem.")

        

L = LSE2()

while True:
    print("1 - Inserir no Inicio")
    print("2 - Inserir no Fim")
    print("3 - Imprimir a Lista")
    print("4 - Remover no Inicio")
    print("5 - Remover no Fim ")
    print("6 - Consultar um Valor")
    print("7 - Transferir um Valor para o Inicio")
    print("8 - Transferir um valor para o Final")
    print("9 - Remover valores repetidos")
    print("0 - Sair do Programa")

    op = int(input("Digite a opcao:"))

    if op == 0:
        break
    elif op == 1:
        val = int(input("Digite o valor a inserir:"))
        L.Ins_Inicio(val) 
    elif op == 2:
        val = int(input("Digite o valor a inserir:"))
        L.Ins_Fim(val) 
    elif op == 3:
        if L.Inicio == None:
            print("Lista vazia!")
        else:
            L.Imprime()
    elif op == 4:
        if L.Inicio == None:
            print("Lista vazia")
        else:
            L.Rem_Inicio()
    elif op == 5:
        if L.Inicio == None:
            print("Lista vazia")
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

    elif op ==8:
        val = int(input("Digite o valor a transferir: "))
        r = L.Consulta(val)
        if r==None:
            print("\nValor nao existe na lista!")
        else:
            if r==L.Fim:
                print("\nJá é o ultimo da lista!")
            else:
                L.Trans_Final(r)

    elif op ==9:
        L.Rem_Oco()
