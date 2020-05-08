#MaBe

lista = []

for obj in range(0,5):
    n = input('Digite um valor: ')
    lista.append(n)

objmin = min(lista)
idmin = lista.index(objmin)
print('Menor valor é {} na posição {}'.format(objmin, idmin))

objmax = max(lista)
idmax = lista.index(objmax)
print('Maior valor é {} na posição {}'.format(objmax, idmax))
