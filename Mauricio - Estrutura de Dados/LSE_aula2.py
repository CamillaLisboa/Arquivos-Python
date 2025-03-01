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

    def setProx(self, val):
        self.prox = val

class LSE:
    def __init__(self):
        self.Inicio = None
        
    def Ins_Inicio(self, val):
        p = No(val)
        p.setProx(self.Inicio)
        self.Inicio = p

    def Ins_Fim(self, val):
        p = No(val)
        if self.Inicio == None:
            self.Inicio = p
        else:
            q = self.Inicio
            while q.getProx() != None:
                q.getProx()
            q.setProx(p)

    def Rem_Inicio(self):
        if self.Inicio.getProx() == None:
            self.Inicio = None
        else:
            self.Inicio = self.Inicio.getProx()

    def Rem_Fim(self):
        if self.Inicio.getProx() == None:
            self.Inicio = None
        else:
            p = self.Inicio
            while p.getProx() != None:
                q = p
                p = p.getProx()
        q.setProx(None)

    def Rem_Cosnulta(self, valor):
    
        if self.Inicio == valor:
            L.Rem_Inicio()
        elif self.Inicio.getProx() == None:
            L.Rem_Fim()
        else:
            p = self.Inicio
            while p != None:
                if p.getInfo() == valor:
                    p.setProx(p.getProx())
                else:
                    p = p.getProx()   


    def Imprime(self):
        p = self.Inicio
        while p != None:
            print(p.getInfo(), '—->', end = '')
            p = p.getProx()
        print("None\n")

    def Consulta(self, val):
        p = self.Inicio
        while (p != None and p.getInfo() != val):
            p = p.getProx()
        return p

L=LSE()
while True:
    
    print("1 - Inserir no Inicio da Lista")
    print("2 - Imprimir Lista")
    print("3 - Inserir no Fim da Lista ")
    print("4 - Remover no Inicio")
    print("5 - Remover no Fim")
    print("6 - Consultar um No")
    print("7 - Remover por Consulta")
    print("0 - Sair do Programa")

    op = int(input())
    
    if op ==0:
        break
    elif op == 1:
        val = int(input())
        L.Ins_Inicio(val)
    elif op == 2:
        if L.Inicio == None:
            print("Lista vazias")
        else:
            L.Imprime()
    elif op == 3:
        val = int(input())
        L.Ins_Fim(val)

    elif op == 4:
        if L.Inicio == None:
            print("lista vazia")
        else:
            L.Rem_Inicio()
    
    elif op == 5:
        if L.Inicio == None:
            print("lista vazia")
        else:
            L.Rem_Fim()

    elif op == 6:
        val = input('digite o valor de pesquisa')
        r = L.Consulta(val)
        if r == None:
            print("valor nao existe na lista")
        else: 
            print('Valor encontrado:', r.getInfo())

    elif op == 7:
        val = input('digite o valor de pesquisa')
        r = L.Consulta(val)

        if L.Inicio == None:
            print(" Lista Vazia")
        elif r == None:
            print("Valor não encontrado na Lista")
        else:
            L.Rem_Cosnulta(r)