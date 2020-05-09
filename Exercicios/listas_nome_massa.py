#MaBe
nomes = []
massas = []
while True:

    nome = input('Digite um nome: ').upper() 
    massa = int(input('Digite a massa: '))

    nomes.append(nome) 
    massas.append(massa)

    r = input('Quer continuar? [s/n] ').lower()

    if r == 'n':
        break

totcad = len(nomes)
pesomai = max(massas)
pesomin = min(massas)

print(nomes)
print(massas)
print(f'{totcad} pessoas cadastradas.')
print(f'O meior peso foi de {pesomai}kg. {nomes[massas.index(pesomai)]}.')
print(f'O menor peso foi de {pesomin}kg. {nomes[massas.index(pesomin)]}.')

