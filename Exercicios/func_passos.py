#MaBe
from time import sleep

def conte(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim}, de ', end='')
    if inicio > fim:
        if passo < 0:
            print(f'{-passo} em {-passo}')
            for n in range(inicio, fim-1, passo):
                print(n, end=' ')
        elif passo == 0:
            print(f'{1} em {1}')
            for n in range(inicio, fim-1, -1):
                print(n, end=' ')
        else:
            print(f'{passo} em {passo}')
            for n in range(inicio, fim-1, -passo):
                print(n, end=' ')
    else: 
        if passo == 0:
            print(f'{1} em {1}')
            for n in range(inicio, fim+1, 1):
                print(n, end=' ')
        
        else:
            print(f'{passo} em {passo}')
            for n in range(inicio, fim+1, passo):
                print(n, end=' ')
        sleep(1)
    print()


conte(1, 10, 1)
print('-'*35)
conte(10, 0, -2)

print('-'*35)
print('Sua vez!')
i = int(input('>>Início da contagem: '))
f = int(input('>>Fim da contagem: '))
p = int(input('>>Passos: '))

conte(i, f, p)