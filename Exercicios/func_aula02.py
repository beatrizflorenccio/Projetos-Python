def somar(a=0, b=0, c=0): #Todos os parâmetros são opcionais
    """
    >> Faz a soma de até 3 valores e exibe o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(c=3, a=2)
somar(9, 2)
somar()