// write program for the heap sort in c

#include<stdio.h>

int main()
{
    int  a[100], n, i, j, temp;

    printf("The program for the heap sort in c \n written by Chirag Singhal \n roll number 2000330100084 \n");

    printf( "Enter the number of elements : " );


    scanf( "%d" , &n);
    printf( "Enter the elements : " );


    for (i = 0; i < n; i++)
        scanf( "%d" , &a[i]);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
    printf( "Sorted array is : " );
    for (i = 0; i < n; i++)
        printf( "%d " , a[i]);

    printf("\n");
    return  0;
}