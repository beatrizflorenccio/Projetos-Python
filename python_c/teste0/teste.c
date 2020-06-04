#include <stdio.h>

int soma(int n1, int n2) {
    int resultado;
    resultado = n1 + n2;
    return(resultado);
    //printf("O resultado e %d", resultado);
}

void main(){
    int s = soma(3, 5);

    printf("soma = %d", s);
}

