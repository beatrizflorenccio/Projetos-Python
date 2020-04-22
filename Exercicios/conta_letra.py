#TRABALHANDO COM STRINGS
#CONTA A QUANTIDADE DE LETRA A NUMA FRASE E INDICA SUAS POSIÇÕES

while True:

    frase = input("Digite uma frase: ").strip().upper()

    if "SAIR" == frase:
        print("saiu", "\n")
        break

    elif "SAIR" != frase:
        print("ANALISANDO FRASE...")
        print("A letra A aparece {} vezes na frase".format(frase.count("A")))
        print("A primeira letra A apareceu na posição {}".format(frase.find("A"))) #find() indica a posição. Procura a partir do lado esquerdo.
        print("A última letra A apareceu na posição {}".format(frase.rfind("A")), "\n") #rfind() indica a posição. Procura a partir do lado direito.
