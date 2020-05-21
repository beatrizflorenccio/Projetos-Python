#MaBe

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [1, 2, 3, 4]
dobra(valores)
print(valores)