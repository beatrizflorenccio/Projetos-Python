#Sistema com a situação de um aluno

dados = {'Nome':input('Nome: '), 'Média':int(input('Média: '))}

if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'

print(f'Nome = {dados["Nome"]}')
print(f'Média = {dados["Média"]}')
print(f'Situação = {dados["Situação"]}')