import cv2
import numpy as np
import pkg_resources 

#encontra o caminho completo até o arquivo.xml
xml = pkg_resources.resource_filename("cv2", "data\\cascade.xml")
print(xml)

h_cascade = cv2.CascadeClassifier(xml) 

img = cv2.imread("pos.jpg")

#Converte para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecta o objeto através do cascade
h = h_cascade.detectMultiScale(gray, 1.3, 10)

#detectMultiScale retorna quatro valores: x, y, w, h
for (x, y, w, h) in h:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2) #Monta o retângulo no objeto detectado


cv2.imshow("img", img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

if k == 13:
    cv2.imwrite("nova.jpg", img) 
    cv2.destroyAllWindows()   
