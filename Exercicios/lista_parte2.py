#MaBe
#Aula de listas parte 2

#Cria as listas
maria = ['Maria', 18]
joao = ['João', 18]
luan = ['Luan', 17]
pedro = ['Pedro', 16]
pessoas = []

#Cria uma ligação entre duas listas
#Dessa forma, toda alteração que eu fizer em maria, também será feita em pessoas e vice versa
#pessoas = maria 

#Faz uma cópia de uma lista
#Dessa forma, as listas são independentes. Uma não interfere na outra.
#pessoas = maria[:]

#Coloca todas essas listas dentro de outra
pessoas = [maria[:], joao[:], luan[:], pedro[:]]
print(pessoas)

#Coloca as listas dentro de outra - modo 2
pessoas2 = []
pessoas2.append(maria[:])
pessoas2.append(joao[:])
pessoas2.append(luan[:])
pessoas2.append(pedro[:])
print(pessoas2, '\n')

#acessando os elementos das listas dentro de uma outra lista
#Elemento 1 da lista 0. Vai exibir 18.
#print(pessoas[0][1]) 

#acessando as sublistas
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])
print(pessoas[3], '\n')

#exemplo de uso com estrutura de repetição
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade!')

print()
#outro exemplo de uso com repetição
#interação com usuário
galera = []
dados = []
for d in range(0, 5):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados = []
print('Dados coletados.')
print(galera)

tmai = 0
tmen = 0
tido = 0

for g in galera:
    if g[1] < 18:
        print(f'{g[0]} é menor de idade')
        tmen += 1
    elif g[1] >= 18 and g[1] < 60:
        print(f'{g[0]} é maior de idade')
        tmai += 1
    elif g[1] >= 60:
        print(f'{g[0]} é idoso')
        tido += 1
      
print(f'Total de {tmen} menores de idade.')
print(f'Total de {tmai} maiores de idade.')
print(f'Total de {tido} idosos.')