dados_gerais = []
while True:

    dados = {
        'nome':input('Nome: '),
        'idade':int(input('Idade: ')),
        'sexo':input('Sexo: [F/M] ').upper()
    }

    dados_gerais.append(dados.copy()) #faz uma cópia do dicionário e manda pra lista

    dados.clear() #limpa o dicionário

    r = input('Continuar? ').lower()
    if r == 'n':
        break

print('-'*40)

total_cadastro = len(dados_gerais) #qtd de pessoas cadastradas
print(f'Foram cadastradas {total_cadastro}')

soma_idade = 0
mulheres = []
for e in range(0, len(dados_gerais)):
    soma_idade += dados_gerais[e]['idade'] #soma as idades 
    if dados_gerais[e]['sexo'] == 'F':
        mulheres.append(dados_gerais[e]['nome']) #add na lista de mulheres
media_idade = round(soma_idade/total_cadastro, 0) #média de idade 

print(f'A média de idade do grupo é {media_idade} anos.')
print(f'As mulheres cadastradas são: {mulheres}')


idade_acima = []
for l in range(0, len(dados_gerais)):
    if dados_gerais[l]['idade'] > media_idade:
        idade_acima.append(dados_gerais[l]['nome'])

print(f'As pessoas com idade acima da média são: {idade_acima}')

#dados_gerais.append(mulheres[:])
#dados_gerais.append(idade_acima[:])









