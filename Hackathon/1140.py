
while True:
    n = input().lower()
    if n != '*':
        char = n[0]
        valid = True

        for i in n.split():
            if i.startswith(char):
                valid = True
            else:
                valid = False
                break

        if valid:
            print('Y')
        else:
            print('N')
    else:
        break

