# Aprendendo a trabalhar com Regex
# Regex é uma expressão regular
# Pode ser usado para verificar se uma sequência contém o padrão de pesquisa especificado

import re # módulo padrão para trabalhar com Regex

# MetaCharacters: caracteres interpretados de maneira especial por um mecanismo Regex
# São eles: [] . ^ $ * + ? {} () \ |
#  [] especifica um CONJUNTO de caracteres que você deseja corresponder

# [abcde] corresponderá se a sequência que está tentando corresponder contiver algum dos caracteres
# [a-e] é o mesmo que [abcde]
# [1-4] é o mesmo que [1234]

# Também pode inverter o conjunto de caracteres para a busca
# [^abcde] corresponderá com qualquer caractere, exceto a ou b ou c ou d ou e

txt = 'abc@123'

x = re.findall('[a-c]', txt) # .Findall() retorna uma lista com as correspondências
print (x)
