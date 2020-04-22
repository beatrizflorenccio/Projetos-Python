#Operações 

''' Algumas anotações importantes:
- Imagens são matrizes Numpy 
- O pixel de origem da img é o pixel (0,0). Canto superior esquerdo. 
- Rrepresentação de pixel no opencv: (y, x)
- O parão de cor é BGR (Azul, Verde, Vermelho)
- Cada canal tem 2 dimensões e vai de 0 a 255 
- Img preto e branco: Apenas um canal
- Img colorida: 3 canais 
- Cada pixel é formado por 3 componentes (B, G, R) de 8 bits cada'''

import cv2 
import numpy as np #operações numéricas 

#Retorna a imagem
#Imagem = matriz Numpy 
img = cv2.imread("foto.jpg")

#Mostrar a altura, a largura e o número de canais de cor da img
info = img.shape #carrega uma tupla com as dimensões da imagem
print("Altura: {}".format(info[0]))
print("Largura: {}".format(info[1]))
print("Canais: {}".format(info[2]))

#Mostrar os canais de cor do pixel (0, 0) da matriz img
(b, g, r) = img[220, 500] 
print("Canal azul: {}".format(b))
print("Canal verde: {}".format(g))
print("Canal vermelho: {}".format(r))
