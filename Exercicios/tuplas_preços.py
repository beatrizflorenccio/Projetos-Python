#Mabe 

produtos = ('caneta', 'lápis', 'borracha', 'corretivo', 'caderno', 'livro', 'estojo', 'mochila', 1.50, 1.00, 3.50, 5.00, 29.90, 45.00, 10.00, 120.00)

t = 'tabela de preços'
print('-=-'*len(t))
print(t)
print('-=-'*len(t))

for pos in range(0, len(produtos[0:8])):
    print(produtos[pos], '.'*30, produtos[pos+8])

