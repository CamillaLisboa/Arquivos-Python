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

def Imprime(Raiz):
    if Raiz != None:
        Imprime(Raiz.getEsq())
        print(Raiz.getInfo(), end=' ')
        Imprime(Raiz.getDir())

def Folhas(Raiz):
    if Raiz != None:
        Folhas(Raiz.getEsq())
        if (Raiz.getEsq()==None and Raiz.getDir()==None):
            print(Raiz.getInfo(), end=' ')
        Folhas(Raiz.getDir())

Raiz = None
Raiz = CAPB(8)
print("\nArvore:\n")
Imprime(Raiz)
print("\nFolhas:\n")
Folhas(Raiz)


















