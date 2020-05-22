#Recebe o ano de nascimento
#Retorna um valor literal indicando voto obrigatório, opcional ou negado.

def voto(ano):
    """
    :param ano: ano de nascimento
    """
    from datetime import datetime #escopo de importação
    id = datetime.now().year - ano
    if 18<= id < 65:
        s = f'Com {id} anos: voto obrigatório'
        return s
        
    elif 16<= id <18 or id>65:
        s = f'Com {id} anos: voto opcional'
        return s
    
    else:
        s = f'Com {id} anos: não vota'
        return s


v1 = voto(int(input('Ano de nascimento: ')))
print(v1)
print(voto(1990))
