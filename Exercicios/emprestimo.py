#MaBe

casa = float(input("Qual o valor da casa? R$ "))
renda = float(input("Qual a sua renda mensal? R$ "))
anos = int(input("Quantos anos de financiamento? "))

prest = casa / (anos * 12) #prestacao mensal
maximo = (renda * 30)/100

if prest <= maximo:
    print("Valor da prestação mensal: {:.2f}".format(prest))
    print(prest)

else:
    print("Valor da prestação mensal: {:.2f}".format(prest))
    print("emprestimo NEGADO")
