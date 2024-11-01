''' Faça um programa em Python que leia uma String e dois caracteres. 
Troque todas as ocorrências do primeiro caracter (podendo ser maiúsculo ou minúsculo)
pelo segundo e imprima a quantidade de vezes que o caracter foi substituido'''

phrase=input().lower()
a,b = input().lower().split()
changes = phrase.count(a)

print(f' total de trocas: {changes}. frase trocada: {phrase.replace(a,b)}')


