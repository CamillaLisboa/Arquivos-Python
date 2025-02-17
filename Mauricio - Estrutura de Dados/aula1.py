def Inserir(lista, nome, n1, n2):
    aluno = [nome,[n1,n2]]
    lista.append(aluno)

def Imprime(alunos):
    for aluno in alunos:
        print(f'Nome:{aluno[0]}. Nota 1: {aluno[1][0]}. Nota 2: {aluno[1][1]}')

def Media(lista, nome):
    for aluno in lista:
        if aluno[0] == nome:
            return (aluno[1][0]+aluno[1][1])/2
        
def InserirInicio(lista, nome, n1, n2):
    aluno = [nome,[n1,n2]]
    lista.insert(0,aluno)

def Buscar(lista, nome):
    for i, item in enumerate(lista):
        if item[0] == nome:
           return i
    return -1
        
                 
       


L= []

while True:
    print("1 - Inseri alunos")
    print("2 - Mostrar os alunos")
    print("3 - Mostrar a media de cada aluno")
    print("4 - Inserir alunos no Inicio")
    print("5 - Consultar aluno por Nome")
    print("6 - Remover um aluno")
    print("0 - Sair do programa")


    op = int(input("Digite a opçao:"))

    if op == 0:
        break
    elif op == 1:
        nome = input("Digite o nome do aluno:")
        nota1 = float(input("Digite a primeira nota:"))
        nota2 = float(input("Digite a segunda nota:"))
        Inserir (L,nome,nota1, nota2)
    elif op == 2:
        if len(L)==0:
            print("Lista vazia")
        else:
            Imprime(L)
    elif op == 3:
        if len(L)==0:
            print("Lista vazia")
        else:
            aluno = input("Digite o nome do aluno:")
            print(f'Media de {aluno} é {Media(L,aluno)}')
    elif op == 4:
        nome = input("Digite o nome do aluno:")
        nota1 = float(input("Digite a primeira nota:"))
        nota2 = float(input("Digite a segunda nota:"))
        InserirInicio (L,nome,nota1, nota2)

    elif op == 5:
        nome = input("Digite o nome do aluno:")
        pos = Buscar(L, nome)
        if pos == -1:
            print(f'Aluno {nome}, não encontrado')
        else:
            print(L[pos])
    
    elif op == 6:
        nome = input("Digite o nome do aluno:")
        pos = Buscar(L, nome)
        if pos == -1:
            print(f'Aluno {nome}, não encontrado')
        else:
            L.pop(pos)
            print(f'Aluno {nome} removido com sucesso!')