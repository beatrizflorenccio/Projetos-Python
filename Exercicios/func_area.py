#MaBe
#Função que calcula a área de um terreno retangular

def area(largura, comprimento):
    area = largura*comprimento
    print(f'A área do terreno é {area}m².')


b = float(input('Largura [m]: '))
h = float(input('Comprimento [m]: '))

area = area(b, h)

