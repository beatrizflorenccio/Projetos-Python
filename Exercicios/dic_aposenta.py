#aposentadoria
from datetime import datetime

data = datetime.now().year #ano corrente

#dados iniciais
nome = {'Nome':input('Nome: '),
        'Idade':(data - int(input('Ano de nascimento: '))),
        'CTPS':int(input('Número da CTPS: (0 se não tiver) '))
}

#se o usuário tiver CTPS... pede informações extras
if nome['CTPS'] != 0:
    nome['Ano de contratação'] = int(input('Ano de contratação: '))
    nome['Salário'] = float(input('Salário: '))
    contribuicao = data - nome['Ano de contratação']
    nome['Aposentadoria'] = 35 - contribuicao + nome['Idade']

print('-'*40) #separando os dados visualmente

for k,v in nome.items():
    print(f'{k} tem o valor {v}')
