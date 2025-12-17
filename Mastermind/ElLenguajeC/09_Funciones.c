#include <stdio.h>

int power(int base, int exponent);


int main() {
    
    power(2, 3);

}




int power(int base, int exponent) {

    int i;
    int result = 1;

    printf("El valor de la base es: %d\n", base);
    printf("El valor del exponente es: %d\n", exponent);

    for (i=1; i <= exponent; i++) {
        result = result * base;
    }

    printf("El resultado de la potencia es: %d\n", result);
    
    return result;

}