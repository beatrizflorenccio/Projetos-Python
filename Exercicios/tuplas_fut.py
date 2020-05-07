#MaBe

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritibua', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('Times: {}'.format(times), '\n')

print('Os 5 primeiros colocados são {}'.format(times[0:6]), '\n')

print('Os últimos 4 colocados são {}'.format(times[16:]), '\n')

print('Em ordem alfabética: {}'.format(sorted(times)), '\n')

print('{} está na {} posição'.format(times[7], times.index('Chapecoense')))
