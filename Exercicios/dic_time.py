time = []
while True: 
    jogador = {}
    jogador = {'Nome':input('Nome: '),
                'Partidas':int(input('Partidas jogadas: ')),
    }

    total_gols = 0
    Gols = []
    for p in range(0, jogador['Partidas']):
        gol = int(input(f'Gols marcados na partida {p+1}: '))
        Gols.append(gol)
        total_gols += gol

    jogador['Total de Gols'] = total_gols
    jogador['Gols por Partida'] = Gols[:]

    time.append(jogador.copy())

    while True:
        r = input('Continuar? [S/N] ').upper()[0]

        if r in 'SN':
            break
        print('ERRO! Preencha com S (sim) ou N (não).')
    
    if r == 'N':
        break


print()
print(f'{"No":<4}{"Nome":<10}{"Gols":>10}{"Total":>30}')
print('='*55)


for i,j in enumerate(time):
    print(f'{i:<4}{j["Nome"]:<10}', end='      ')
    print(f'{j["Gols por Partida"]}', end='               ')
    print(f'{j["Total de Gols"]}')

while True:

    while True:
        resp = int(input('Mostrar desempenho de qual jogador? '))

        if resp <= len(time):
            break
        print('ERRO! Jogador inexistente.')

    if resp == 999:
        break

    print('--Desempenho do Jogador--')
    for j, g in enumerate(time[resp]["Gols por Partida"]):
        print(f'No jogo {j+1} marcou {g} gols')

