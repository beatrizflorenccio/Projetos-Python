#MaBe

#Criando a matriz
matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor da posição {(c, l)}: '))

#Organizando 
for obj in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[obj][i]}]', end=' ')
    print()    

#Somando os valores pares
soma = 0
for id in range(0,3):
    for k in range(0, 3):
        if matriz[id][k] % 2 == 0:
            soma += matriz[id][k]

#Somando os valores da terceira coluna
ult = 0
for a in range(0,3):
    ult += matriz[a][2]

#Maior valor da segunda linha
maival = max(matriz[1])

print(f'Soma dos números pares: {soma}')
print(f'Soma dos valores da terceira coluna: {ult}')
print(f'Maior valor da segunda linha: {maival}')
