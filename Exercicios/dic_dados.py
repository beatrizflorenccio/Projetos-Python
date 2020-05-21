from operator import itemgetter

galera = []
pessoa = {}
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = input('Idade: ')

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
print(f'Temos {len(galera)} pessoas cadastradas.')



    


   
 





