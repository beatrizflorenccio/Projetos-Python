
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

print('-'*40)

for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('-'*40)

print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas:')
for i in range(0, jogador['Partidas']):
    print('>'*4, f'Na partida {i+1}, marcou {jogador["Gols por Partida"][i]}')

print(f'Total de {total_gols} gols.')