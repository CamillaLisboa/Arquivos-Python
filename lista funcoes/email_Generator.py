def getName(entrada):
    entrada = entrada.split()
    nome = entrada[0]
    sobrenome = entrada[-1]
    return nome, sobrenome

def createEmail(name, surname, emails):
    email = f'{name}.{surname}@dominio.com'
    unique = verifyEmail(email, emails)
    if unique == 0:
        return email
    return f'{name}.{surname}{unique}@dominio.com'

def verifyEmail(email, emails):
    partes = email.split('@')
    parte1 = partes[0]
    count = sum(1 for e in emails if e.startswith(parte1))
    return count

emails = []

while True:
    entrada = input('Insira seu nome completo ou "exit" para sair ---> ').lower()
    if entrada != 'exit':
        nome, sobrenome = getName(entrada)
        email = createEmail(nome, sobrenome, emails)
        emails.append(email)
    else:
        print(emails)
        break
