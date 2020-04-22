#MARIA BEATRIZ

v = int(input("Qual a velocidade do carro? "))

if v <= 80:
    print("Você está dentro do limite!")

elif v > 80:
    print("MULTADO! Você excedeu o limite de 80km/h")
    multa = float((v - 80) * 7)
    print("A multa é de {} reais".format(multa))

print("Tenha um bom dia!")
