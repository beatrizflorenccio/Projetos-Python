from random import randint
from time import sleep
from operator import itemgetter

nums = {'jogador1':randint(1, 6),
        'jogador2':randint(1, 6),
        'jogador3':randint(1, 6),
        'jogador4':randint(1, 6),
}

for k,v in nums.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

#nums.itens() para ele retornar tanto as keys quanto os values
#key=itemgetter() para dizer o parâmetro da ordem
#key=itemgetter(0) ordena de acordo com as keys
#key=itemgetter(1) ordena de acordo com os values
ranking = sorted(nums.items(), key=itemgetter(1))

print('\nRANKING DOS JOGADORES')

for i,v in enumerate(ranking):
    print('>'*(i+1), f'{i+1}º lugar: {v[0]} com {v[1]} no dado')
    sleep(1)