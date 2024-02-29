#include <stdio.h>

int main()
{
    for(int i = 1; i <= 20; i++)
    {
        printf("%d ", i);
    }
    
    printf("\n");

    int checkIfEven = -10;
    while (checkIfEven <= 10)
    {
        if (checkIfEven % 2 == 0)
        {
            printf("%d ", checkIfEven);
        }
        checkIfEven++;
    }

}
