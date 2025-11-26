#include <stdio.h>

int main(){
    int c, nl;

    nl = 0;
    c = getchar();

    while (c != EOF)
    {
        if (c == '\n')
        {
            ++nl;
        }
        c = getchar();
    }
    
    printf("%d\n", nl);
}