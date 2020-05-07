#Desafio Mundo 3 - curso

num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Numero invalido. ', end='')

print('Voce digitou o numero {}'.format(num[n]))    