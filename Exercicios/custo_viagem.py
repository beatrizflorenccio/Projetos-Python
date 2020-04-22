#MaBe
import math 

dist = int(input("Qual a distância de sua viagem? "))

if dist <= 200.0:
    custo = dist*0,50

else:
    custo = dist*0,45

print("O valor de sua passagem será de {} reais".format(custo))
