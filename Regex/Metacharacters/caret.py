# Metacharacter caret ^
# Usado para verificar se uma expressão começa com alguma coisa
import re

txt = 'instituto'

x = re.search('[^i]', txt)
