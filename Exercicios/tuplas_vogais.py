#MaBe

tupla = ('carro', 'casa', 'caneta', 'mercado', 'doente', 'pandemia')

for pala in tupla:
    print('\n', 'Na palavra {} temos '.format(pala), end='')
    for letra in pala:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


