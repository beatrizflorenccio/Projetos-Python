#MaBe
#ANSI escape sequence
#Modelo: \033[style; text; backm
#Style: 0(sem estilo), 1(negrito), 4(sublinhado), 7(inverte)
#text: 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(magenta), 36(ciano) e 37(cinza padrao)
#back: 40 a 47

print("Olá! Prazer em te conhecer, {}".format("\33[1;32mMARIA\33[m"))
