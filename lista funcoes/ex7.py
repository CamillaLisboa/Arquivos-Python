def separa_data(data):
    dia = data[:2] 
    mes = data[2:4]
    ano = data[4:]
    return dia, mes, ano

def verify_mes(mes,ano):
    ano = bissexto(ano)
    if mes == 2 and ano == True:
        return 29
    elif mes == 2 and ano == False:
        return 28
    elif mes in ['04','06','09','11'] :
        return 30
    return 31

def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False
    
entrada = input()
dia,mes,ano = separa_data(entrada)
