#MaBe

lista = []

while True:

    n = int(input('Digite um valor: '))

    if n in lista:
        print('Esse valor já existe. Tente outro.')

    elif n not in lista:
        lista.append(n)
        print('Adicionado.')
        r = input('Continuar? [S/N] ')

        if r.lower() == 'n':
            print(lista) 
            break       

