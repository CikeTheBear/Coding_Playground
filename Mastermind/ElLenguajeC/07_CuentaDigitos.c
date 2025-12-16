#include <stdio.h>

int main () {
        int c, nwhite, nother;
        int ndigit;

        nwhite=nother=ndigit=0;


        while ((c = getchar()) != EOF) {
            if (c == ' ' || c == '\n' || c == '\t') {
                ++nwhite;
            }
            else if (c >= '0' && c <= '9') {
                ++ndigit;
            }
            else {
                ++nother;
            }
        }


        printf("espacios en blanco: %d, otros: %d\n", nwhite, nother);
        printf("digitos: %d/n", ndigit);






}