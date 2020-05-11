#MaBe


matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor da posição {(c, l)}: '))

for obj in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[obj][i]}]', end=' ')
    print()    
