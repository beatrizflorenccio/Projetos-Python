# Methacaracter interrogacao ?
# Usado para zero ou uma ocorrencia do padrao restante

import re

txt = 'man' #1
txt2 = 'maan' #2
txt3 = 'main' #0
txt4 = 'mn' #1

lista = [txt, txt2, txt3, txt4]
tam = len(lista)

for i in range(0, tam):
    x = re.findall('ma?n', lista[i])
    print(x)