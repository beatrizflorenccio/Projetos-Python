#MaBe

num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))   

print(num)

print('O valor 9 apareceu {}x'.format(num.count(9)))

if 3 in num:
    print('O valor 3 foi digitado primeiro na posição {}'.format(num.index(3)))
else:
    print('Não existe o valor 3 na tupla')

print('Os valores pares são: ')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')


