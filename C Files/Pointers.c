#include <stdio.h>

int main()
{
  int a,b;
    int *ptr;

    //Assigns the address of 'a' to the pointer
    ptr = &a;
    //Assigns the value '1234' to the address in the pointer
    *ptr = 1234;
    //Assigns the address of 'b' to the pointer
    ptr = &b;
    //Assigns the value '4567' to the address in the pointer
    *ptr = 4567;

    //Print the value of 'a' (1234) and 'b' (4567)
    printf("A is %d and B is %d\n",a,b);
  
  return 0;
}
