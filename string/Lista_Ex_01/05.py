''' Fazer um programa em Pythonh para verificar se uma determinada String é palíndronio.'''

word = input()

if word == word[::-1]:
    print(f' a palavra "{word}" é um palíndrono')
else:
    print(f'a palavra "{word}" não é um palíndrono')