#include <stdio.h>
#include <stdlib.h>

// El rand debe ser entre 97 y 122 (letras minusculas en ASCII)

int main() {

    int vidas = 10;
    int fin = 0;
    int letraSecreta = 'm';
    int letraUsuario = '\n';

    while (vidas > 0 && fin == 0) {

        printf("\nAdivina la letra secreta: ");
        letraUsuario = getchar();
        getchar(); // Consumir el salto de linea

        if (letraUsuario == letraSecreta) { //Ganar
            printf("\nHas ganado!\n");
            fin = 1;
        }

        else if (letraUsuario != letraSecreta) {
            vidas--;
            printf("\nFallaste, te quedan %d vidas\n", vidas); //Perder
            if (vidas <= 0) {
                printf("\nHas perdido!, la letra secreta era '%c'\n", letraSecreta);
            }
        }
    }
}