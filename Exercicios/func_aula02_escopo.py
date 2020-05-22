#Escopo de variáveis. Aula 21 Python Mundo 3

#Escopo local
def teste():
    x = 8 #Foi declarada dentro da função, logo a variável é local. Só vai funcionar nessa área.
    d = 1 #Cria uma variável nova. Local. Diferente do d global. 
    print(f'Na função teste, a variável local x tem valor {x}')
    print(f'Na função teste, a variável global n tem valor {n}')
    print(f'Na função teste, a variável local d tem valor {d}')

#Escopo global: 
d = 5
n = 4
print(f'No programa principal, n global vale {n}')
#print(f'No programa principal, x vale {x}'). Vai dar erro, pois x é uma variável local.
print(f'No programa principal, d global vale {d}')

teste()

print('\nEu também posso optar por alterar a variável global d dentro da minha função, em vez de o python criar uma versão local dela:')
def teste2():
    global d
    d = 2
    print(f'Na função teste2, d global vale {d}')

print(f'No programa principal, d global também vale {d}')