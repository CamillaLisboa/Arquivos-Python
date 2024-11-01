while True:
    frase = input().strip()
    if frase == "*":
        break

    palavras = frase.lower().split()
    inicial = palavras[0][0]

    tautograma = all(palavra[0] == inicial for palavra in palavras)

    if tautograma:
        print("Y")
    else:
        print("N")