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

def Busca(Raiz, val):
    if Raiz is None:
        return None
    else:
        if Raiz.info == val:
            return Raiz
        else:
            if Raiz.info > val:
                return Busca(Raiz.esq, val)
            else:
                return Busca(Raiz.dir, val)

def BuscaSemRec(Raiz, val):
    while Raiz is not None:
        if Raiz is None:
            return None
        else:
            if Raiz.info == val:
                return Raiz
            else:          
                if Raiz.info > val:
                    Raiz = Raiz.esq
                else:
                    Raiz = Raiz.dir

def Busca_Pai(Raiz, r):
    if Raiz.dir == r or Raiz.esq == r:
        return Raiz
    else:
        if Raiz.info > r.info:
            return Busca_Pai(Raiz.esq, r)
        else:
            return Busca_Pai(Raiz.dir, r)
        
def Remove(Raiz, val):
    r = Busca(Raiz, val)

    pai = Busca_Pai(Raiz, r)

    if r.esq is None and r.dir is None:
        if pai.esq == r:
            pai.esq = None
        else:
            pai.dir = None
    elif r.esq is None or r.dir is None:
        filho = r.esq if r.esq else r.dir
        if pai.esq == r:
            pai.esq = filho
        else:
            pai.dir = filho
    else:
        sucessor = r.dir
        pai_sucessor = r
        while sucessor.esq:
            pai_sucessor = sucessor
            sucessor = sucessor.esq

        r.info = sucessor.info 

        if pai_sucessor.esq == sucessor:
            pai_sucessor.esq = sucessor.dir
        else:
            pai_sucessor.dir = sucessor.dir

    return Raiz

    
Raiz = None

A = [50, 80, 60, 70, 65, 30, 40, 20, 35, 10, 15, 90, 100]

while True:
    print("\n\n1 - Inserir Chaves")
    print("2 - Percursos")
    print("3 - Buscar Valor")
    print("4 - Buscar sem Recursividade")
    print("5 - Buscar pai de um Nó")
    print("6 - Remover um valor")
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

    elif op==3:
        val = int(input("Insira o valor: "))
        r = Busca(Raiz, val)

        if r is None:
            print("\nValor não existe na árvore!")
        else:
            print("\nValor encontrado: ", r.info)

    elif op==4:
        val = int(input("Insira o valor: "))
        r = BuscaSemRec(Raiz, val)

        if r is None:
            print("\nValor não existe na árvore!")
        else:
            print("\nValor encontrado: ", r.info)

    elif op==5:
        val = int(input("Insira o valor: "))
        r = Busca(Raiz, val)

        if r is None:
            print("\nValor não existe na árvore!")
        else:
            if r==Raiz:
                print("\nRaiz não tem pai!")
            else:
                pai = Busca_Pai(Raiz, r)
                print("\nO pai de", r.info,"=", pai.info)

    elif op==6:
        val = int(input("Insira o valor a ser removido: "))
        r = Busca(Raiz, val) 

        if r==None:
            print("\nValor não existe na árvore!")
        else:
            if r==Raiz:
                print("\nNão é permitido remover a Raiz!")
            else:
                Remove(Raiz, val)
                print("\nValor removido com sucesso!")

 
        


    