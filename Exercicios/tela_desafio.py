import PySimpleGUI as sg


class Tela:
    def __init__(self):
        estrutura = [
        [sg.Text("Nome: ", size=(6,0)), sg.Input(size=(20,0), key="n")],
        [sg.Text("Idade: ", size=(6,0)), sg.Input(size=(3,0), key="i")],
        [sg.Button("Enviar Dados")],
        [sg.Output(size=(50,20))]
        ]

        #Criando a janela
        self.janela = sg.Window("Desafio Jaguar").layout(estrutura)

    def Iniciar(self):
        dados = []
        while True:
            self.button, self.values = self.janela.Read()
            Nome = self.values["n"]
            dados.append(Nome)
            Idade = int(self.values["i"])

            if Idade <18:
                Idade = "menor de idade"
                dados.append(Idade) #insere a idade na lista
                print(dados)

            elif Idade >=18 and Idade <65:
                Idade = "maior de idade"
                dados.append(Idade)
                print(dados)

            elif Idade >=65:
                Idade = "idoso"
                dados.append(Idade)
                print(dados)


tela = Tela()
tela.Iniciar()
