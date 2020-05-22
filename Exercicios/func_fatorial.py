def fatorial(num=1, show=False):
    """
    >> Calcula o Fatorial de um numero.
    :param num: numero
    :param show: Mostrar ou nao a conta. True ou False
    :return: O valor do fatorial de um numero num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            f *= c
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        else:
            f *= c
    return f



print(fatorial(5))
print(fatorial(5, show=True))
help(fatorial)