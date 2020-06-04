cdef soma(int n1, int n2):
    r = n1 + n2
    return r

if __name__ == '__main__':
    x = soma(3, 4)
    print(x)