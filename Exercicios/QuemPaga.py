import random
import time

titulo = "QUEM PAGA A CONTA?"
print()
print("=" * len(titulo))
print(titulo)
print("=" * len(titulo))
print("para sair digite 0 no campo de candidato")
print()

while True:
    nomes = []
    n = int(input("QUANTOS ROLEZEIROS IRÃO NO ROLÊ? "))

    if n != 0:

        for bebados in range(1, n+1):
            a1 = input("{}º CANDIDATO: ".format(bebados))
            nomes.append(a1)

        sorteio = random.shuffle(nomes)
        sorteio = random.choice(nomes)

        print("\33[1;31mO ESCOLHIDO É...\33[m")
        time.sleep(1)
        print("{}! BEM FEITO HAHAHA! Ele que lute.".format(sorteio))
        print()

    else:
        print("saiu")
        print()
        break
