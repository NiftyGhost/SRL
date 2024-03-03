#include <stdio.h>

int main()
{
  int pokey = 2009;
  int *p;

  p = &pokey;
  //Both print out the address of the 'pokey' variable.
  printf("The address of 'pokey' is %p\n", &pokey);
  printf("The address of 'p' is %p\n", p);

  //Both print out the value of the 'pokey' variale.
  printf("The value of 'pokey' is %d\n", pokey);
  printff("The valueof 'p' is %d\n", *p);
  
  return 0;
}
