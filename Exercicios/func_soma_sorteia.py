from random import randint 
from time import sleep

#Função que sorteia 5 números e joga numa lista
def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for cont in range(0, 5): #laço
        n = randint(1,10) #randomiza valores inteiros entre 1 e 10
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

#Função que soma os pares da lista
def pares(lista):
    pares = 0 #soma dos pares
    for e in nums: #para cada elemento de nums
        if e % 2 == 0: #se o resto da divisão por 2 for 0
            pares += e
    print(f'Somando os valores pares de {nums}, temos {pares}')

nums = []
sorteia(nums)
pares(nums)