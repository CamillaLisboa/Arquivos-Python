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
                q = q.getProx()
            q.setProx(p)

    def Ins_Depois(self, r, val):
        p = No(val)
        p.setProx(r.getProx())
        r.setProx(p)

    def Ins_Antes(self, r, val):
        p = self.Inicio
        while p.getProx() != r:
            p = p.getProx()

        novo_no = No(val)
        novo_no.setProx(r)
        p.setProx(novo_no)

    def Ins_Ordem(self,val):
        if self.Inicio == None or val < self.Inicio.getInfo():
            self.Ins_Inicio(val)
        else:
            p = self.Inicio
            while p is not None:
                if p.getInfo() < val:
                    p=p.getProx()
                else:
                    self.Ins_Antes(p,val)
            self.Ins_Fim(p, val) 

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

    def Rem_Cosnulta(self, r):
        p = self.Inicio
        while p.getProx() != r:
            p = p.getProx()
         
        p.setProx(r.getProx())


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
    print("8 - Inserir depois de um valor")
    print("9 - Inserir antes de um valor")
    print("10 - Inserir de forma Ordenada")
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
        val = int(input('digite o valor de pesquisa'))
        r = L.Consulta(val)
        if r == None:
            print("valor nao existe na lista")
        else: 
            print('Valor encontrado:', r.getInfo())

    elif op == 7:
        val = int(input('digite o valor de pesquisa'))
        r = L.Consulta(val)

        if r == None:
            print("Valor não encontrado")
        else:
            if r == L.Inicio:
                L.Rem_Inicio()
            else:
                if r.getProx() == None:
                    L.Rem_Fim()
                else:
                    L.Rem_Cosnulta(r)

    elif op == 8:
        val = int(input('digite o valor de pesquisa'))
        r = L.Consulta(val)
        if r == None:
            print("valor nao existe na lista")
        else: 
            val = int(input("Digite o valor a inserir"))
            if r.getProx() == None:
                L.Ins_Fim(val)
            else:
                L.Ins_Depois(r,val)

    elif op == 9:
        val = int(input('digite o valor de pesquisa'))
        r = L.Consulta(val)
        if r == None:
            print("valor nao existe na lista")
        else: 
            val = int(input("Digite o valor a inserir"))
            if r==L.Inicip():
                L.Ins_Inicio(val)
            else:
                L.Ins_Antes(r,val)

    elif op == 10:
        val = int(input("Digite o valor a inserir"))
        L.Ins_Ordem(L, val)