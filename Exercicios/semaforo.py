#MaBe
import time

print()
print("=" * 30)
print("\33[1;38;48mSEMÁFORO\33[m".center(43))
print("=" * 30)

t1 = int(input("Tempo para o vermelho: "))
t2 = int(input("Tempo para o amarelo: "))
t3 = int(input("Tempo para o verde: "))

print()
print("INICIANDO SISTEMA...")
time.sleep(1)

#Vermelho
print()
print("\33[1; 31mVermelho: LIGADO\33[m")
print("\33[1mAmarelo: DESLIGADO\33[m")
print("\33[1mVerde: DESLIGADO\33[m")
for x in range(t1, -1, -1):
    print(">>>Tempo: {}s".format(x))
    time.sleep(1)


#Amarelo
print()
print("\33[1mVermelho: DESLIGADO\33[m")
print("\33[1; 33mAmarelo: LIGADO\33[m")
print("\33[1mVerde: DESLIGADO\33[m")
for y in range(t2, -1, -1):
    print(">>>Tempo: {}s".format(y))
    time.sleep(1)

#Verde
print()
print("\33[1mVermelho: DESLIGADO\33[m")
print("\33[1mAmarelo: DESLIGADO\33[m")
print("\33[1; 32mVerde: LIGADO\33[m")
for z in range(t3, -1, -1):
    print(">>>Tempo: {}s".format(z))
    time.sleep(1)
print()
