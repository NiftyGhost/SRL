#include <stdio.h>

int main()
{
    int array[] = {11,13,17,19};
    int *ptr;

    //Location of the entire array (and it's first element)
    ptr = array;

    //Prints the first element of the array
    printf("The element is %d\n", *ptr);

    for(int x = 0; x < 4; x++)
    {
        //Prints the value of the current element of the array
        printf("Element %d is %d\n", x + 1, *ptr);
        //Prints the address of the current element of the array
        printf("It's in address %p\n", ptr);

        //Goes to the next address of the array
        ptr++;
        //or ptr = ptr + 1;
    }

    return 0;
}
