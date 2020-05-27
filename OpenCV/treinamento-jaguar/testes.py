#treinamento opencv jaguar

import cv2
import numpy as np 
from matplotlib import pyplot as grafico

img =  cv2.imread("C:\\Users\\maria\\Documents\\GitHub\\Projetos-Python\\OpenCV\\treinamento-jaguar\\Imagens\\fruta.png", 0)

cv2.imshow("teste", img)

imgclara = cv2.add(img, 40)
cv2.imshow("cinza", imgclara)

h=cv2.calcHist([img], [0], None, [256], [0,256])

imgeq = cv2.equalizeHist(img)

cv2.imshow("equalizada", imgeq)

cv2.waitKey(0)
cv2.destroyAllWindows()