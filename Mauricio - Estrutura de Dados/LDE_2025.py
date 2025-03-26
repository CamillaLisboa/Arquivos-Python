class No:
    def __init__(self, val):
        self.esq = None
        self.info = val
        self.dir = None

    def getEsq(self):
        return self.esq

    def getDir(self):
        return self.dir

    def getInfo(self):
        return self.info

    def setEsq(self, x):
        self.esq = x

    def setDir(self, x):
        self.dir = x

    def setInfo(self, x):
        self.info = x

class LDE:
    def __init__(self):
        self.Inicio = None
        self.Fim = None

    def Ins_Inicio(self, val):
        p = No(val)
        if self.Inicio==None:  #lista vazia
            self.Inicio = p
            self.Fim = p
        else:
            p.setDir(self.Inicio)
            self.Inicio.setEsq(p)
            self.Inicio = p

    def Ins_Fim(self, val):
        p = No(val)
        if self.Inicio == None:  # lista vazia
            self.Inicio = p
            self.Fim = p
        else:
            p.setEsq(self.Fim)
            self.Fim.setDir(p)
            self.Fim = p

    def Imprime(self):
        p = self.Inicio
        print("\nNone", end='')
        while p != None:
            print("<--", p.getInfo(),"-->",end='')
            p = p.getDir()
        print(None)

    def Rem_Inicio(self):
        if self.Inicio==self.Fim:  #só existe 1 nó
            self.Inicio = None
            self.Fim = None
        else:
            self.Inicio = self.Inicio.getDir()
            self.Inicio.setEsq(None)

    



L = LDE()
while True:
    print("\n1 - Inserir no Inicio")
    print("2 - Inserir no Fim")
    print("3 - Imprimir a Lista")
    print("4 - Remover no Inicio")
    print("5 - Remover no Fim")

    print("0 - Sair do programa")
    op = int(input("\nDigite a opcao: "))

    if op==0:
        break
    elif op==1:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Inicio(val)

    elif op==2:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Fim(val)

    elif op==3:
        if L.Inicio==None:
            print("\nLista Vazia!\n")
        else:
            L.Imprime()

    elif op==4:
        if L.Inicio==None:
            print("\nLista Vazia!\n")
        else:
            L.Rem_Inicio()



