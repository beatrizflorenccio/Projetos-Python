#aposentadoria
from datetime import datetime

data = datetime.now().year

nome = {'Nome':input('Nome: '),
        'Idade':(data - int(input('Ano de nascimento: '))),
        'CTPS':int(input('Número da CTPS: (0 se não tiver) '))
}

if nome['CTPS'] != 0:
    nome['Ano de contratação'] = int(input('Ano de contratação: '))
    nome['Salário'] = float(input('Salário: '))
    contribuicao = data - nome['Ano de contratação']
    nome['Aposentadoria'] = 35 - contribuicao + nome['Idade']

print('-'*40)

for k,v in nome.items():
    print(f'{k} tem o valor {v}')
