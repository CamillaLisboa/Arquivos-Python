
from validadata import *
            
while True:
    entrada = input()
    if validaEntrada(entrada):
        print('Entrada correta')
        if validaData(entrada):
           print('Data válida!')
           break
        else:
            print('Data inválida!')
    else:
        print('Entrada incorreta.')
    print('Digite novamente.....')

