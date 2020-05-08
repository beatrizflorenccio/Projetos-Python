#MaBe
lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    r = input('Quer continuar? [s/n] ')

    if r == 'n':
        print('Foram digitados {} números'.format(len(lista)))
        print(sorted(lista, key=int, reverse=True))

        if 5 in lista:
            print('Número 5 está na posição {}'.format(lista.index(5)))
        elif 5 not in lista:
            print('Número 5 não existe na lista.') 
        break       


