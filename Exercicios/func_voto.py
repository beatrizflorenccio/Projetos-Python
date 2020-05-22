#Recebe o ano de nascimento
#Retorna um valor literal indicando voto obrigatório, opcional ou negado.

from datetime import datetime

def voto(ano=datetime.now().year):
    """
    :param ano: ano de nascimento
    """
    id = datetime.now().year - ano
    s = ''
    if id >= 18:
        s = 'obrigatório'
        return s
    elif 16<= id <18:
        s = 'opcional'
        return s
    else:
        s = 'negado'
        return s

v1 = voto(2018)
v2 = voto(2002)
v3 = voto()
v4 =  voto(2003)

print(f'As situação dos pedidos são: \n{v1} \n{v2} \n{v3} \n{v4}')
