#include <stdio.h>
#include <stdlib.h>

// El rand debe ser entre 97 y 122 (letras minusculas en ASCII)

int main() {

    int vidas = 10;
    int fin = 0;
    int letraSecreta = 'm';
    int letraUsuario = '\n';

    do {
        letraUsuario = getchar();
    }

    while (vidas > 0 && fin == 0); {
        printf("Adivina la letra secreta: ");
        letraUsuario = getchar();

        if (letraUsuario == letraSecreta) { //Ganar
            printf("Has ganado!\n");
            fin = 1;
        }

        else if (letraUsuario != letraSecreta) {
            vidas--;
            printf("Fallaste, te quedan %d vidas\n", vidas); //Perder
            if (vidas <= 0) {
                printf("Has perdido!, la letra secreta era '%c'\n", letraSecreta);
            }
        }
    }





















}