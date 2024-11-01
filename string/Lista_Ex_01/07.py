''' Elabore um programa em python que lê um string e calcule e imprima um codigo utilizando a seguinte regra:
para cada vogal, somar 5 pontos, para cada consoante somar 10 pontos,
desconsiderando qualquer outro caracter'''

from unidecode import unidecode

text = input()
vowels = 'aeiou'
score = 0

for char in unidecode(text.lower()).replace(' ',''):
    if char in vowels:
        score+=5
    else:
        score+=10

print(f'Código = {score}')
