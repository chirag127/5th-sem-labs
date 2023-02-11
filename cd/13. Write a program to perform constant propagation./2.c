#include <stdio.h>
#include <string.h>
struct op
{
    char l;
    char r[20];
} op[10], pr[10];
void main()
{
    int a, i, k, j, n, z = 0, m, q;
    char *p, *l;
    char temp, t;
    char *temp;
    printf("Enter the no.of values");
    scanf("% d", &n);
    for (i = 0; i < n; i++)
    {
        printf("\tleft\t");
        op[i].l = getchar();
        printf("\tright\t");
        scanf("% s", op[i].r);
    }

                printf("eliminate common sub expression\n");
                for (i = 0; i < z; i++)
                    printf("% c\t =", pr[i].l);
                printf("% s\n", pr[i].r);
                // duplicate production elimination
                for (i = 0; i < z; i++)
                {
                    for (j = i + 1; j < z; j++)
                    {
                        q = strcmp(pr[i].r, pr[j].r);
                        if ((pr[i].l == pr[j].l) && !q)
                        {
                            pr[i].l =’\0’;
                            strcpy(pr[i].r,’\0’);
                        }
                    }
                }
                printf("optimized code");
                for (i = 0; i < z; i++)
                {
                    if (pr[i].l !=’\0’)
                    {
                        printf("% c =", pr[i].l);
                        printf("% s\n", pr[i].r);
                    }
                }
                getch();
}
