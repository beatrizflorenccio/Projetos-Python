#EQUIPE JAGUAR
import random

print()
print("-=-" * 20)
print("Sou seu computador!", "\nVou pensar num número entre 0 e 10. Tente adivinhar!")
print("-=-" * 20)
print()
maquina = random.randint(0, 10)

usuario = int(input("E aí, em que número eu pensei? "))

while usuario != maquina:

    if usuario > maquina:
        print("ops, errado! é menor... tente de novo.")
        usuario = int(input("Qual o palpite? "))

    elif usuario < maquina:
        print("ops, errado! é maior... tente de novo.")
        usuario = int(input("Qual o palpite? "))

print("Isso mesmo, você acertou!")
print()
