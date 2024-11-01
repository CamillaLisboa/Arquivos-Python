from validadata import *
from datetime import date

def calculaIdade(data):
    dia, mes, ano = map(int, data.split('/'))
    hoje = date.today()
    idade = hoje.year - ano - ((hoje.month,hoje.day)< (mes,dia))
    return idade

while True:
    birth = input()
    if validaEntrada(birth):
        if validaData(birth):
            break
        else:
            print('Data inválida')
    else:
        print('Entrada Inválida')
    print('Digite novamente...')

print(f'Idade: {calculaIdade(birth)} anos')