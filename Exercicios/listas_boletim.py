alunos = []

while True:

    nome = input('Aluno: ')
    n1 = float(input('Nota 01: '))
    n2 = float(input('Nota 02: '))
    m = ((n1+n2)/2)

    alunos.append([nome, n1, n2, m])

    r = input('Quer continuar? [s/n] ').lower()

    if r == 'n':
        break
    
print('-=-'*30)

print(f'{"No":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)

for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8}')

while True:

    resp = int(input('Mostrar nota de qual aluno? '))

    if resp == 999:
        break

    if resp <= len(alunos) - 1:
        print(f'As notas de {alunos[resp][0]} são: {alunos[resp][1:3]}')

