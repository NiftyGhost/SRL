#include <stdio.h>
#include <string.h>

int main()
{
    char firstSentence [] = "Thinking about Yukari and Persona 3 Reload motivates me to keep studying. ";
    char secondSentence [] = "I also have to keep studying to achieve my dreams.\n";
    char combinedSentence[64];

    strcpy(combinedSentence, firstSentence);
    strcat(combinedSentence, secondSentence);

    puts(combinedSentence);

    return 0;
}