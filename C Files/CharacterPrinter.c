#include <stdio.h>

int main()
{
    /*                          *\
    |  How to print a character  |
    \*                          */

    printf("Input something: ");
    int aCharacter;
    scanf("%d", &aCharacter);
    //OR
    putchar(aCharacter);

    //OR

    int anotherCharacter = getchar();
    printf("%c", anotherCharacter);
    //OR
    //putchar(anotherCharacter);

    return 0;
}
