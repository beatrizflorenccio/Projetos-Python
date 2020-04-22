#MaBe
#Le um ano e diz se é bissexto ou nao 

from datetime import date

ano = int(input("Digite o ano que deseja analisar: "))

if ano == 0:
    ano = date.today().year

if ano % 400 == 0 or ano % 100 != 0 and ano % 4 == 0:
    print("Ano BISSEXTO!")

else:
    print("Ano NÃO BISSEXTO!")
