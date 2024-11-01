''' Escreva um programa em Python que leia uma palavra fornecida pelo teclado
e em seguida escreva o caracter presente no meio da palavra, caso esta tenha
um número ímpar de caracteres e os dois do meio caso par'''

word = input()
leng = len(word)
if leng % 2 == 0:
    print(word[leng//2-1], word[leng//2] )
else:
    print(word[leng//2])