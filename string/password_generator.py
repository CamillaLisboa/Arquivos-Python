'''
Faça um programa em Python que gera uma senha aleatória de 8 digitos tendo 1 maiúscula, 1 minúscula e 1 número
'''
import string
from random import choice, sample, shuffle

password = []

password.append(choice(string.ascii_lowercase)) 
password.append(choice(string.ascii_uppercase))
password.append(choice(string.digits))

for char in range(5):
    password.append(choice(string.ascii_letters + string.digits))

#instead of using 'for/in', sample does the same thing

password.extend(sample(string.ascii_letters + string.digits, 5)) 
shuffle(password)

password = ''.join(password)
print(password)
