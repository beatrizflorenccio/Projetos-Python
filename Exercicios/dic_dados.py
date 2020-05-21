from operator import itemgetter

galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    soma+= pessoa['idade']

    while True:
        pessoa['sexo'] = input('Sexo: ').upper()[0] #caixa alta e considera apenas a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('INVÁLIDO! Digite somente F ou M. ')
    galera.append(pessoa.copy())
    while True:
        r = input('Quer continuar? [S/N]').upper()[0]
        if r in 'SN':
            break
        print('INVÁLIDO! Digite somente S ou N. ')

    if r == 'N':
        break

print('-'*40)
print(f'A) Temos {len(galera)} pessoas cadastradas.')

media = soma/len(galera) #média da idade
print(f'B) A média de idade é de {media:2.2f} anos')
print('C) As mulheres cadastradas foram:', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')

print('\nD) Lista das pessoas com idades acima da média: ')
for p in galera:
    if p['idade'] > media:
        print()
        for k,v in p.items():
            print(f'{k} = {v};', end=' ')






