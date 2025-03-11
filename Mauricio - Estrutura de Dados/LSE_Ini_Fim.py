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
            print(f'{p.getInfo()} --->',end=' ')
            p = p.getProx()

        print("None")

    def Rem_Inicio(self):
        p = self.Inicio
        
        if p.getProx() == None:
            self.Inicio = None
            self.Fim = None
        else:
            self.Inicio = p.getProx()

    def Rem_Fim(self):
        p = self.Inicio

        while p.getProx() != self.Fim:
            p = p.getProx()
        
        p.setProx(None)
        self.Fim = p


L = LSE2()

while True:
    print("1 - Inserir no Inicio")
    print("2 - Inserir no Fim")
    print("3 - Imprimir a Lista")
    print("4 - Remover no Inicio")
    print("5 - Remover no Fim ")
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
