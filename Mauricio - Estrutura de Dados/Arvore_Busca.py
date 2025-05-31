class No_arvore:
    def __init__(self, val):
        self.esq = None
        self.info = val
        self.dir = None

def Insere(Raiz, No):
    if Raiz.info < No.info:
        if Raiz.dir == None:
            Raiz.dir = No
        else:
            Insere(Raiz.dir, No)
    else:
        if Raiz.esq == None:
            Raiz.esq = No
        else:
            Insere(Raiz.esq, No)

def In_Order(Raiz):
    if Raiz != None:
        In_Order(Raiz.esq)
        print(Raiz.info, end=' ')
        In_Order(Raiz.dir)

def Pre_Order(Raiz):
    if Raiz != None:
        print(Raiz.info, end=" ")
        Pre_Order(Raiz.esq)
        Pre_Order(Raiz.dir)

def Pos_Order(Raiz):
    if Raiz != None:
        Pos_Order(Raiz.esq)
        Pos_Order(Raiz.dir)
        print(Raiz.info, end=" ")
    
Raiz = None

A = [50, 80, 60, 70, 65, 30, 40, 20, 35, 10, 15, 90, 100]

while True:
    print("\n\n1 - Inserir Chaves")
    print("2 - Percursos")
    print("0 - Sair do Programa")

    op= int(input("Digite a opção: "))

    if op==0:
        break

    elif op==1:
        for val in A:
            No = No_arvore(val)
            if Raiz is None:
                Raiz = No
            else:
                Insere(Raiz, No)

    elif op==2:
        print("PRE: ")
        Pre_Order(Raiz)

        print("\nIN: ")
        In_Order(Raiz)

        print("\nPOS: ")
        Pos_Order(Raiz)
