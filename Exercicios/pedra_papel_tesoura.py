#MaBe
import random
import time

print()
print("-=-" * 20)
print("\33[1;34mJOGO PEDRA, PAPEL, TESOURA!\33[m")
print("-=-" * 20)
print("\nSuas opções:", "\nPEDRA[0]", "\nPAPEL[1]", "\nTESOURA[2]")

itens = ["PEDRA", "PAPEL", "TESOURA"]
maquina = random.randint(0,2)
jogador = int(input("\nQual a sua jogada? "))

print("\nJO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!", "\n")
time.sleep(1)

print("A maquina jogou {}".format(itens[maquina]))
print("O Jogador jogou {}".format(itens[jogador]), "\n")
time.sleep(1)

if maquina == 0:
    if jogador == 0:
        print("\33[1;33mEMPATE!\33[m Vamos de novo!", "\n")
    elif jogador == 1:
        print("\33[1;32mJOGADOR venceu!\33[m", "\n")
    elif jogador == 2:
        print("\33[1;32mMAQUINA venceu!\33[m", "\n")

elif maquina == 1:
    if jogador == 0:
        print("\33[1;32mMAQUINA venceu!\33[m", "\n")
    elif jogador == 1:
        print("\33[1;33mEMPATE!\33[m Vamos de novo!", "\n")
    if jogador == 2:
        print("\33[1;32mJOGADOR venceu!\33[m", "\n")


elif maquina == 2:
    if jogador == 0:
        print("\33[1;32mJOGADOR venceu!\33[m", "\n")
    elif jogador == 1:
        print("\33[1;32mMAQUINA venceu!\33[m", "\n")
    if jogador == 2:
        print("\33[1;33mEMPATE!\33[m Vamos de novo!", "\n")
