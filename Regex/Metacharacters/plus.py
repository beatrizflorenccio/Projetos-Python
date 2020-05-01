# Methacaracter plus +
# Usado para uma ou mais correspondencias do padrao restante 

import re

txt = 'maaano'

x = re.findall('ma+n', txt)
print (x)