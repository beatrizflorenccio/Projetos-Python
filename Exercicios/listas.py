#MaBe

lista = [4, 1, 10, 8]

#alterando valores da lista
lista[1] = 0

#inserir obj no fim da lista
lista.append(7)

#ordem crescente
lista.sort()

#ordem decrescente
lista.sort(reverse=True)

#inserir obj numa pos específica
lista.insert(1, 6)

#remove
lista.remove(4)

#retorna index e o obj
for c, v in enumerate(lista):
    print('Posição {} e valor {}'.format(c, v))