#Escopo de variáveis. Aula 21 Python Mundo 3

#Escopo local
def teste():
    x = 8 #Foi declarada dentro da função, logo a variável é local. Só vai funcionar nessa área.
    d = 1 #Essa variável d é != da variável d global. Essa aqui é local.
    print(f'Na função teste, a variável x tem valor {x}')
    print(f'Na função teste, a variável n tem valor {n}')
    print(f'Na função teste, a variável d tem valor {d}')

#Escopo global: 
d = 5
n = 4
print(f'No programa principal, n vale {n}')
#print(f'No programa principal, x vale {x}'). Vai dar erro, pois x é uma variável local.
print(f'No programa principal, d vale {d}')

teste()