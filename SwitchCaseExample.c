#include <stdio.h>

int main () 
{
    char aLetter;
    scnaf("%c", aLetter);
    switch(aLetter)
    {
        case 'Y':
        case 'y':
            puts("Yukari?");
            break;
        case 'M':
        case 'm':
            puts("Mitsuru?");
            break;
        default:
            puts("Erm.");
    }
    
    return 0;
}