def validaEntrada(data):
    if len(data) != 10 or data[2] != '/' or data[5] != '/':
        return False
    if not data.replace('/','').isdigit():
        return False
    return True

def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

def validaData(data):
    dia, mes, ano = map(int, data.split('/'))
    if mes == 2:
        if bissexto(ano):
            if 1 <= dia <= 29:
                return True
        else:
            if 1 <= dia <= 28:
                return True
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
                return True
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
                return True
    return False