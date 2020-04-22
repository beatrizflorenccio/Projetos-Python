#MaBe
import time

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
op = 0

while op != 5:

    print("[1] Somar", "\n[2] Multiplicar", "\n[3] Maior valor", "\n[4] Novos numeros", "\n[5] Sair")
    op = int(input("Qual opção você escolhe? "))

    if op == 1:
        result = n1 + n2
        time.sleep(1)
        print("A soma entre {} e {} é {}".format(n1, n2, result))
        print("=-=" * 14)
        time.sleep(2)

    elif op == 2:
        result = n1 * n2
        time.sleep(1)
        print("A multiplicação entre {} e {} é {}".format(n1, n2, result))
        print("=-=" * 14)
        time.sleep(2)

    elif op == 3:
        if n1 > n2:
            result = n1
        else:
            result = n2
        time.sleep(1)
        print("O maior valor {} e {} é {}".format(n1, n2, result))
        print("=-=" * 14)
        time.sleep(2)

    elif op == 4:
        print("Informe os números novamente.")
        time.sleep(1)
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        time.sleep(1)

    else:
        print("Opção inválida. Tente novamente.")
        print()


print("Você está fora do jogo! Até mais.")
print()
