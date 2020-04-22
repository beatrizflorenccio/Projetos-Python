#Salvando uma imagem

import cv2 

id = 0 #index da câmera
local = "img_salva.png" #nome da imagem que será salva
camera = cv2.VideoCapture(id) #Inicia a câmera

print("Para sair, tecle Esc", "\nPara salvar a imagem, tecle Enter")

while True:

    retval, img = camera.read() #Lê a camera
    cv2.imshow("Video", img) #Exibe a imagem

    k = cv2.waitKey(100)

    #Se o usuário teclar Enter 
    if k == 13: #13 é a key para a tecla ENTER
        cv2.imwrite(local, img)
        print("Imagem salva")
        break

    #Se o usuário teclar Esc    
    elif k == 27: #27 é a key para a tecla Esc
        print("Nenhuma imagem salva")
        print("Você Saiu")
        break

cv2.destroyAllWindows()
camera.release()