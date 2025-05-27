class NO:
    def __init__(self, val):
        self.esq = None
        self.info = val
        self.dir = None

    def getEsq(self):
        return self.esq

    def getInfo(self):
        return self.info

    def getDir(self):
        return self.dir

    def setEsq(self, x):
        self.esq = x

    def setInfo(self, x):
        self.info = x

    def setDir(self, x):
        self.dir = x


def CAPB(n):
    if n==0:
        r = None
    else:
        val = int(input("Digite o valor: "))
        r = NO(val)
        r.setEsq(CAPB(n//2))
        r.setDir(CAPB(n-n//2-1))

    return r

def In_Order(Raiz):
    if Raiz != None:
        In_Order(Raiz.getEsq())
        print(Raiz.getInfo(), end=' ')
        In_Order(Raiz.getDir())

def Pre_Order(Raiz):
    if Raiz != None:
        print(Raiz.getInfo(), end=" ")
        Pre_Order(Raiz.getEsq())
        Pre_Order(Raiz.getDir())

def Pos_Order(Raiz):
    if Raiz != None:
        Pos_Order(Raiz.getEsq())
        Pos_Order(Raiz.getDir())
        print(Raiz.getInfo(), end=" ")

def Folhas(Raiz):
    if Raiz != None:
        Folhas(Raiz.getEsq())
        if (Raiz.getEsq()==None and Raiz.getDir()==None):
            print(Raiz.getInfo(), end=' ')
        Folhas(Raiz.getDir())


Raiz = None
Raiz = CAPB(8)
print("\nArvore:\n")
print("\n PRE:", end=" ")
Pre_Order(Raiz)
print("\n IN :", end=" ")
In_Order(Raiz)
print("\n POS:", end=" ")
Pos_Order(Raiz)
print("\n Folhas:", end=" ")
Folhas(Raiz)

