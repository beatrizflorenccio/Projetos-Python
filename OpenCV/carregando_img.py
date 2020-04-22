#Carregando uma imagem

import cv2 

#cv2.imread("nome do arquivo de img", flag)
#Careggar imagem em preto e branco: flag = 0
#Carregar imagem colorida: flag = 1
img = cv2.imread("logo.png", 0) 

#Exibe a imagem carregada na tela
#cv2.imshow("nome da janela (qualquer nome que queira", imagem carregada)
cv2.imshow("Imagem", img)

#cv2.waitKey(delay em milisegundos)
#Espera que o usuário digite algo para fechar a janela
#Para que a janela não abra e feche rapidamente
cv2.waitKey(0)

#Destroi todas as janelas abertas com o programa
cv2.destroyAllWindows()



