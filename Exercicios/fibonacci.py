#MaBe

print()
print("-" * 22)
print("\33[1; 33mSEQUÊNCIA DE FIBONACCI\33[m")
print("-" * 22)

qtd = int(input("Quantos termos deseja exibir? "))
print()

t1 = 0
t2 = 1
pos = 3
result = print("{} -> {}".format(t1, t2), end="")

while pos <= qtd:
    t3 = t1 + t2
    print("-> {}".format(t3), end="")
    t1 = t2
    t2 = t3
    pos += 1
print()
print("FIM!")
print("-" * 22)
print()
