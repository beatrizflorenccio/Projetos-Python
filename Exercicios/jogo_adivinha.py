#EQUIPE JAGUAR 2020

from random import randint #Carrega o método randint do módulo random. randint randomiza um numero inteiro
import time

print()
print("-=-" * 20, "\nVou pensar num numero entre 0 e 5. Tente adivinhar!", "\nPara sair do jogo digite sair.")
print("-=-" * 20, "\n")


while True:

    maquina = str(randint(0, 5))
    usuario = input("Em que numero eu pensei? ").upper().strip()

    if usuario == "SAIR":
        print("SAINDO...")
        time.sleep(2)
        print("você saiu do jogo!", "\n")
        break

    elif usuario == maquina:
        print("PROCESSANDO...")
        time.sleep(2)
        print("VOCÊ GANHOU! Vamos de novo, amigo!", "\n")

    elif usuario != maquina:
        print("\33[0;33mPROCESSANDO...\33[m")
        time.sleep(2)
        print("EU GANHEI! Eu pensei no número {} e não no número {}.Vamos de novo.".format(maquina, usuario), "\n")
