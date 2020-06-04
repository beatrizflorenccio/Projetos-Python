from ctypes import cdll

libteste = cdll.LoadLibrary("./libteste.so")

x = libteste.soma(2, 5)
print (x)