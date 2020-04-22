from urllib import request 
from urllib.request import urlretrieve
import urllib
import numpy as np
import cv2
import os

#link_negativas = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03445777' 
link_negativas = 'Coloque aqui o link das urls das imagens negativas'
urls_negativas = urllib.request.urlopen(link_negativas).read().decode() #abre as urls
#print(urls_negativas)

print("problema ao carregar as urls")    

#Se nao existir uma pasta chamada "negativas"
if not os.path.exists("negativas"):
    os.makedirs("negativas") #cria uma pasta chamada "negativas"

numero_imagem = 1 #nome da primeira imagem

#Para cada url presente na lista
for url in urls_negativas.splitlines(): #divide a sequencia de urls em uma lista. Cada url sera um elemento. 
    try:

        print(url)

        #nomeia a imagem
        urllib.request.urlretrieve(url, "negativas/"+str(numero_imagem)+".jpg") #redireciona para a pasta negativas 
        
        img = cv2.imread("negativas/"+str(numero_imagem)+".jpg",cv2.IMREAD_GRAYSCALE) #le em escala de cinza a img redirecionada para a pasta negativas 
        img_redimensionada = cv2.resize(img, (100,100)) #redimensiona a imagem
        cv2.imwrite("negativas/"+str(numero_imagem)+".jpg",img_redimensionada) #salva a imagem na pasta negativas
        numero_imagem += 1 #nome da proxima imagem

    except Exception as e:
        print(str(e))