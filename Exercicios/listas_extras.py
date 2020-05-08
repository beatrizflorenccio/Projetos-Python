#MaBe

lista1 = []
lista2 =[]
lista3 = []

while True:
    n = int(input('Digite um valor: '))
    lista1.append(n)
    r = input('Continuar? [s/n] ')

    if r.lower() == 'n':
        for obj in lista1:
            if obj % 2 == 0:
                lista2.append(obj)
            elif obj % 2 != 0:
                lista3.append(obj)
        break

print('Os valores digitador foram: {}'.format(lista1))
print('Os pares são: {}'.format(lista2))
print('Os ímpares são: {}'.format(lista3))                    

    
