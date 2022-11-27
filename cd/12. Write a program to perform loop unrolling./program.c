//  Write a program to perform loop unrolling.

#include <stdio.h>
void main()
{
    unsigned int n;
    int x;
    char ch;
    printf("\nEnter N\n");
    scanf("%u", &n);
    x = countbit(n);
    printf("\nAfter Loop UnRoll, Count of iterations :  %d", x);
}

int countbit(unsigned int n)
{
    int bits = 0, i = 0;
    while (n != 0)
    {
        if (n & 1)
            bits++;
        if (n & 2)
            bits++;
        if (n & 4)
            bits++;
        if (n & 8)
            bits++;
        n >>= 4;
        i++;
    }
    return bits;
}