import PySimpleGUI as sg

class Tela:
    def __init__(self):

        #Tema da janela. Paleta de cores.
        #sg.theme("DarkAmber") 

        #Todas as coisas dentro da janela
        layout = [
        [sg.Text("Nome", size=(5,0)), sg.Input(size=(15, 0), key="nome")],
        [sg.Text("Idade", size=(5, 0)), sg.Input(size=(15, 0), key="idade")],
        [sg.Text("Provedores de email aceitos:")],
        [sg.Checkbox("Gmail", key="gmail"), sg.Checkbox("Outlook", key="outlook"), sg.Checkbox("Yahoo", key="yahoo")],
        [sg.Text("Aceita cartão")],
        [sg.Radio("Sim", "cartões", key="aceita"), sg.Radio("Não", "cartões", key="não aceita")],
        [sg.Button("Enviar dados")],
        [sg.Output(size=(50, 20))]]

        #Criando a janela
        self.janela = sg.Window("Dados dos usuários").layout(layout)

    def Inicia(self):
        while True:
            #Extrai os dados da atela
            self.button, self.values = self.janela.Read()
            nome = self.values["nome"]
            idade = self.values["idade"]
            gmail = self.values["gmail"]
            outlook = self.values["outlook"]
            yahoo = self.values["yahoo"]
            aceita_cartão = self.values["aceita"]
            não_aceita_cartão = self.values["não aceita"]
            print()
            print("nome: {}".format(nome))
            print("idade: {}".format(idade))
            print("gmail: {}".format(gmail))
            print("outlook: {}".format(outlook))
            print("yahoo: {}".format(yahoo))
            print("Aceita cartão: {}".format(aceita_cartão))
            print("Não aceita cartão: {}".format(não_aceita_cartão))
            print()

tela = Tela()
tela.Inicia()
