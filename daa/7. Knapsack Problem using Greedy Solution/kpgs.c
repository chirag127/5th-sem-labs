// write a program for the knapsack problem using greedy solution in c

#include<stdio.h>

int main()
{
    int  n, i, j, temp, m, p[100], w[100], x[100], tp = 0, tw = 0;
    float  u;

    printf("This is the program for the knapsack problem using greedy solution in c \n written by Chirag Singhal \n roll number 2000330100084 \n");

    printf( "Enter the number of objects : " );
    scanf( "%d" , &n);
    printf( "Enter the weights and profits of each object : " );
    for (i = 0; i < n; i++)
        scanf( "%d %d" , &w[i], &p[i]);
    printf( "Enter the capacity of knapsack : " );
    scanf( "%d" , &m);
    for (i = 0; i < n; i++)
        x[i] = 0;
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++)
            if (p[i] < p[j])
            {
                temp = p[i];
                p[i] = p[j];
                p[j] = temp;
                temp = w[i];
                w[i] = w[j];
                w[j] = temp;
            }
    u = m;
    for (i = 0; i < n; i++)
    {
        if (w[i] > u)
            break;
        else
        {
            x[i] = 1;
            tw = tw + w[i];
            tp = tp + p[i];
            u = u - w[i];
        }
    }
    if (i < n)
        x[i] = u / w[i];
    tw = tw + (u * x[i]);
    tp = tp + (p[i] * x[i]);
    printf( "The result vector is : " );
    for (i = 0; i < n; i++)
        printf( "%d " , x[i]);
    printf( "Maximum profit is : %d " , tp);

    printf("\n");
    return  0;
}