#DESAFIO EQUIPE JAGUAR - 2020

dados = []
while True:

    nome = input('Digite seu nome: ').strip().upper()
    if nome == "SAIR":
        print("Voce saiu!")
        break

    if nome != "SAIR":
        dados.append(nome)
        idade = int(input('Digite sua idade: '))

        if idade <18:
            idade = "menor de idade"
            dados.append(idade)
            print(dados)

        elif idade >= 18 and idade <65:
            idade = "maior de idade"
            dados.append(idade)
            print(dados)

        else:
            idade = "idoso"
            dados.append(idade)
            print(dados)
