#MaBe
#Le um numero e diz se é par ou impar

n = int(input("Digite um numero qualquer: "))
res = n % 2 #fornece o resto da divisão por 2

if res == 0:
    print("Numero par!")
else:
    print("Numero impar!")    
