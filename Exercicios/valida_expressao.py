#MaBe
#Exercício 083     
#Validação de expressões

exp = input('Digite a expressão: ')

abertos = exp.count('(')
fechados = exp.count(')')
#print(abertos)
#print(fechados)

if abertos > fechados:
    print('Falta de fechamento de parênteses')

elif fechados > abertos:
    print('Excesso de fechamento de parênteses')

elif fechados == abertos:
    print('Expressão válida!')    