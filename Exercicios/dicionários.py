#Aula de dicionários. Mundo 03.

pessoas = {'nome':'Maria', 'sexo':'F', 'idade':18}
#Se estiver dento de aspas simples, usar aspas duplas, como abaixo
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-'*40)

#Exibir as keys
print(pessoas.keys())
print('-'*40)

#Exibindo os valores das keys
print(pessoas.values())
print('-'*40)

#Exibindo os items (keys e valores juntos)
print(pessoas.items())
print('-'*40)

#acessando as keys por laços
for k in pessoas.keys():
    print(k)

print('-'*40)

#acessando os values por laços
for v in pessoas.values():
    print(v)

print('-'*40)

#acessando as keys e os values por laços
for k,v in pessoas.items():
    print(f'{k} = {v}')

print('-'*40)

#apagando um item da lista
del pessoas['sexo']
for k,v in pessoas.items():
    print(f'{k} = {v}')

print('-'*40)

#alterando o valor de um item
pessoas['nome'] = 'Beatriz'
for k,v in pessoas.items():
    print(f'{k} = {v}')

print('-'*40)

#Adicionando um item ao dicionário
pessoas['massa'] = 55.4
for k,v in pessoas.items():
    print(f'{k} = {v}')

print('-'*40)

#Dicionário dentro de lista
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil = []
print(estado1)
print(estado2)
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf']) 
print(brasil[1]['sigla'])

print('-'*40)

