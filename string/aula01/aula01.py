'''
list() transforma a string em lista onde cada caracter é um objeto.
''.join() une todos os caracteres da lista e retorna como string
'''

name = 'Camillo'
n= list(name)
n[6]='a'
s=''.join(n)
print(s)

word = "Brasília"
