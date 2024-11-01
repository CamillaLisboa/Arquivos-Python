def verifica_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if len(pilha) == 0:
                return "incorrect"
            pilha.pop()
    if len(pilha) == 0:
        return "correct"
    else:
        return "incorrect"

while True:
    try:
        expressao = input().strip()
        resultado = verifica_parenteses(expressao)
        print(resultado)
    except EOFError:
        break
