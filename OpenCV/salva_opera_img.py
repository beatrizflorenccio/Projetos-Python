import cv2
import numpy as np 

camera = cv2.VideoCapture(0)

while True:
    retval, img = camera.read()
    cv2.imshow("Imagem", img)

    k = cv2.waitKey(100) #Espera até que o usuário aperte uma tecla para parar

    if k == 13:
        cv2.imwrite("foto.jpg", img) #salva a img no disco
        img_salva = cv2.imread("foto.jpg") #lê a img salva 

        info = img_salva.shape #retorna as dimensões da img em uma tupla

        (b, g, r) = img_salva[240, 320] #informação do pixel tal nos canais da img

        print("Altura da img: {} pixels".format(info[0]))
        print("Largura da img: {} pixels".format(info[1]))
        print("Canais: {}".format(info[2]))

        print ("Canal azul: {}".format(b))
        print("Canal verde: {}".format(g))
        print("Canal vermelho: {}".format(r))
        
    elif k == 27: #Se apertar a tecla Esc
        print("Saiu")  
        break  

cv2.destroyAllWindows()
camera.release()

