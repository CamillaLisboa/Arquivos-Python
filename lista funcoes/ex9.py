
from datetime import date

def trocaMes(data):
    mes=data.month
    dia = data.day
    ano = data.year
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 
           'maio', 'junho', 'julho', 'agosto', 
           'setembro', 'outubro', 'novembro', 'dezembro']
    return f'{dia} de {meses[mes - 1]} de {ano}'


data= date.today()
print(f'Data de hoje: {trocaMes(data)}')   