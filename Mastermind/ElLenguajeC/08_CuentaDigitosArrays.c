#include <stdio.h>

int main()
{

    int c, nwhite, nother;
    int ndigit[10];
    int i;

    for (i = 0; i < 10; ++i)
    {
        ndigit[i] = 0;
    }

    nwhite = 0;
    nother = 0;

    while ((c = getchar()) != EOF)
    {
        if (c == ' ' || c == '\n' || c == '\t')
        {
            ++nwhite;
        }
        else if (c >= '0' && c <= '9')
        {
            if (c == '0')
                ++ndigit[0];
            else if (c == '1')
                ++ndigit[1];
            else if (c == '2')
                ++ndigit[2];
            else if (c == '3')
                ++ndigit[3];
            else if (c == '4')
                ++ndigit[4];
            else if (c == '5')
                ++ndigit[5];
            else if (c == '6')
                ++ndigit[6];
            else if (c == '7')
                ++ndigit[7];
            else if (c == '8')
                ++ndigit[8];
            else if (c == '9')
                ++ndigit[9];
        }
        else
        {
            ++nother;
        }
    }

    printf("Espacios en blanco: %d\n", nwhite);
    printf("Otros caracteres: %d\n", nother);
    for (i = 0; i < 10; ++i)
    {
        printf("El digito %d aparecio %d veces\n", i, ndigit[i]);
    }
}