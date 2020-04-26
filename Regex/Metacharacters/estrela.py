# Metacharacter estrela *
# Zero ou mais ocorrencias do último caractere
import re

txt = 'woman'
txt2 = 'main'
txt3 = 'maaan'

x = re.findall('ma*n', txt)
print(x)
