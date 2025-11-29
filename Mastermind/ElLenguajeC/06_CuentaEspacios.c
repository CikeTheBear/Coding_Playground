#include <stdio.h>


int main() {

    int c, nwhite, nother;
    int ndigit;

    nwhite=nother=ndigit=0;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            ++nwhite;
        }
        else if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9') {
            ++ndigit;
        }
        else {
            ++nother;
        }
    }

    printf("espacios en blanco: %d, digitos: %d, otros caracteres: %d\n", nwhite, ndigit, nother);



}