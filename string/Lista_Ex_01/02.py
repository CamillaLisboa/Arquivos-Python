''' Faça um programa em Python que leia uma frase e imprima quantas
 vogais tem esta frase. Considerar minúscula e maiúscula'''

phrase = input()
vowels = 'aeiouAEIOU'
total = 0
for char in phrase:
    if char in vowels:
        total+=1

print(f'Total de voagais na frase "{phrase}" é: {total}')

