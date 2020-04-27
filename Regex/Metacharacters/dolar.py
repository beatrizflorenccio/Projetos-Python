# Metacharacter dolar
# Usado para verificar correspondencia no final da expressão

import re

txt = 'robocup'

x = re.search('[p$]', txt)

if x != None:
    print('correspondencia encontrada')
else:
    print('nao corresponde')
