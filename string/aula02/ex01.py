t = 'um tigre, dois tigres, tres tigres'

p=0

while (p > -1):
    p = t.find('tigre',p)
    if p >= 0:
        print(f'Posição: {p}')
        p+=1

