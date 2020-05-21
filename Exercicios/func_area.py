#MaBe

def area(largura, comprimento):
    area = largura*comprimento
    print(f'A área do terreno é {area}.')


b = int(input('Largura [m]: '))
h = int(input('Comprimento [m]: '))

area = area(b, h)

print(f'A área do de terreno é de {area}m2')
