#include <stdio.h>
#include <string.h>

int main()
{
char firstString[] = "I love Yukari! ";
    char secondString[] = "She's just so cute!\n";
    char buffer[64];

    strcpy(buffer,firstString);
    strcat(buffer,secondString);

    printf("%s", buffer);

    return 0;
}
