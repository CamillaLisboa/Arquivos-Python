alunos = {}

def add_aluno():
    nome = input("Digite o nome do aluno: ")
    notas = list(map(float, input("Digite as notas separadas por espaço ").split()))
    alunos[nome] = notas
    print(f"{nome} foi adicionado(a) com sucesso!")

def update_aluno():
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        nota = float(input("Digite a nova nota: "))
        alunos[nome].append(nota)
        print(f"Aluno {nome} atualizado com sucesso.")
    else:
        print(f"Aluno {nome} inválido.")

def mostar_notas():
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        print(f"{nome}: {alunos[nome]}")
    else:
        print(f"Aluno {nome} não encontrado")

def mostrar_media():
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        media = sum(alunos[nome]) / len(alunos[nome])
        print(f"Média do aluno {nome}: {media:.2f}")
    else:
        print(f"Aluno {nome} não encontrado")

def media_turma():
    if alunos:
        for nome, notas in alunos.items():
            media = sum(notas) / len(notas)
            print(f"Nome: {nome}, média: {media:.2f}")
    else:
        print("Nenhum aluno cadastrado.")

def menu():
    while True:
        print("\n1. Adicionar novo alunos e suas notas.")
        print("2. Update aluno.")
        print("3. Exibir notas de aluno cadastrado.")
        print("4. Exibir média de aluno cadastrado")
        print("5. Exibir média de todos os alunos")
        print("6. Sair")

        opcao = int(input("Escolha a opção desejada: "))
        
        if opcao == 1:
            add_aluno()
        elif opcao == 2:
            update_aluno()
        elif opcao == 3:
            mostar_notas()
        elif opcao == 4:
            mostrar_media()
        elif opcao == 5:
            media_turma()
        elif opcao == 6:
            print("Finalizando programa...")
            break
        else:
            print("Opção inválida. Tente novamente")

menu()