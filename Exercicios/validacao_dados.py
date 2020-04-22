#MaBe

sexo = input("Digite seu sexo: [M/F] ").strip().upper()

while sexo not in "FM":
    sexo = input("Dado inválido! Por favor, informe seu sexo: ").strip().upper()
print("Sexo {} registrado com sucesso!".format(sexo))
