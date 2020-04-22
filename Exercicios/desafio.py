#DESAFIO DO PROCESSO SELETIVO DE 2020 - JAGUAR
#Mabe S2

dados = [] #lista vazia dos dados

while True:
    #dados = [] #lista vazia dos dados

    nome = input("Digite seu nome: ").strip().upper() #usuario digita um nome. strip() elimina os espaços.
    if nome == "SAIR": #Se o usuario digitar sair, para a execucao
        print("voce saiu!")
        break

    if nome != "SAIR": #Se o usuario entrar com um nome, continua
        dados.append(nome) #insere o nome na lista
        idade = int(input("Digite a sua idade: ")) #usuario digita uma idade
        #Foi utilizado int() para tratar a idade como numero inteiro
        #Se estiver usando Python 2, utilize raw_input()


        if idade <18:
            idade = "menor de idade"
            dados.append(idade) #insere a idade na lista
            print(dados)

        elif idade >=18 and idade <65:
            idade = "maior de idade"
            dados.append(idade)
            print(dados)

        else:
            idade = "idoso"
            dados.append(idade)
            print(dados)
