

def maior(*int):
    print('-'*50)
    print('Analisando...')
    if len(int) >=0:
        for n in int:
            print(n, end=' ')
        print(f'Foram recebidos {len(int)} parâmetros inteiros')
        print(f'O maior inteiro é {max(int)}')
    elif int :
        print(f'Foram recebidos {len(int)} parâmetros inteiros')
        print(f'O maior inteiro é {len(int)}')
    print('-'*50)

maior(0)