#Varre a img toda
#Altera cada pixel

import cv2 
import numpy as np 

camera = cv2.VideoCapture(0) 

while True:
    retval, img = camera.read() 
    cv2.imshow("kakaka", img)

    k = cv2.waitKey(100) #Espera o usuário apertar alguma tecla para parar
    

    if k == 13: #Se apertar a tecla Enter
        cv2.imwrite("salva.jpg", img)
        salva = cv2.imread("salva.jpg")

        infoy = salva.shape[0] #altura
        infox = salva.shape[1] #largura

        for y in range(0, infoy):
            for x in range(0, infox):
                salva[y, x] = (255, 0, 0)

        cv2.imshow("imagem modificada", salva)
        

    elif k == 27: #Se apertar a tecla Esc
        break

cv2.destroyAllWindows()
camera.release()        



