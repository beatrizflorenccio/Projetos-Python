#MaBe
from datetime import date

maiores = 0
menores = 0

for id in range(1, 8):
    ano = int(input("Ano de nascimento da {}° pessoa: ".format(id)))
    idade = (date.today().year) - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1


print("{} são maiores de idade e {} são menores de idade".format(maiores, menores))
