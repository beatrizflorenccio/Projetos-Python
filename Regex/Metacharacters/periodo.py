# Metacharacter periodo .
# Um periodo corresponde a qualquer caractere unico
import re

txt = 'maria'

x = re.findall('[mar.]', txt)
print (x)
