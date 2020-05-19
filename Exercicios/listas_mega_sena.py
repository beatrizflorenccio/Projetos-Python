#Jogo da Mega Sena
from random import randint
from time import sleep

#cabeçalho
title = 'JOGUE NA MEGA SENA'
print('-'*len(title))
print(title)
print('-'*len(title))

#Pede ao usuário a qtd de jogos
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'>> Entendido, vou sortear {qtd} jogos')

#Lista para armazenar os números dos jogos
jogo = []
jogos = []

for j in range(0, qtd):
    for c in range(0, 6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:]) #faz uma cópia do jogo e salva na lista de todos os jogos
    jogo.clear()
    print(f'Jogo {j+1}: {jogos[j]}')
    sleep(1)



