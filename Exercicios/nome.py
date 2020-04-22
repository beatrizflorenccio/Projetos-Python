#LÊ UM NOME COMPLETO E DIZ QUAL O PRIMEIRO NOME E QUAL O ÚLTIMO NOME

while True:

    nome = input("Digite seu nome completo: ").upper().strip()
    n1 = nome.split() #fatia o nome. Divide em partes. Joga para uma lista.

    ult = len(n1) - 1 #len() conta as posições da lista. Me da a quantidade.
    ult = n1[ult] #fornece o útimo nome
    prim = n1[0] #posição 0 da lista é o primeiro nome

    if nome == "SAIR":
        print("saiu", "\n")
        break

    elif nome != "SAIR":
        print("Seu primeiro nome é {}".format(prim), "\nSeu último nome é {}".format(ult), "\n" )
