#MaBe
import random
import time

print()
print("IDENTIFICADOR DE CORNO")

while True:

    a1 = input("NOME DO SUSPEITO: ").strip().lower()

    if a1 == "sair":
        print("\33[1; 31mchifrudo saindo...\33[m")
        print("tchau, corno")
        print()
        break

    elif a1 != "sair":
        a2 = "É CORNO! Adora um papel de trouxa..."
        a3 = "NÃO É CORNO... não ainda"
        cornos = [a2, a3]
        corno = random.shuffle(cornos) #mexe na ordem
        corno = random.choice(cornos) #seleciona um
        print("\33[1;31mVERIFICANDO...\33[m")
        time.sleep(1)
        print(corno)
        print()
