#include <stdio.h>
#include <string.h>

int main () 
{
    /*                          *\
    |   Ways to print a String   |
    \*                          */

    printf("Input anything: ");
    char userInput[64];
    //Using stdio.h
    fgets(userInput,64,stdin);
    puts(userInput);
    //OR
    printf("%s\n", userInput);

    //char yukariComplement[] = "Yukari is a very in-depth character.";
    //puts(yukariComplement);
}