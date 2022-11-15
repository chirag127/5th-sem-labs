
#include<stdio.h>

#include<string.h>

char s[20], st[20];

int main()

{

    char m[5][6][3] = {"tb", " ", " ", "tb", " ", " ", " ", "+tb", " ", " ", "n", "n", "fc", " ", " ", "fc", " ", " ", " ", "n", "*fc", " a ", "n", "n", "i", " ", " ", "(e)", " ", " "};

    int s[5][6] = {2, 0, 0, 2, 0, 0, 0, 3, 0, 0, 1, 1, 2, 0, 0, 2, 0, 0, 0, 1, 3, 0, 1, 1, 1, 0, 0, 3, 0, 0};

    int i, j, k, n, s1, s2;


    printf("\nEnter the input string: ");

    scanf("%s", s);

    strcat(s, "$");

    n = strlen(s);

    st[0] = '$';

    st[1] = 'e';

    i = 1;

    j = 0;

    printf("\nstack     Input\n");

    printf("__________________\n");

    while ((st[i] != '$') && (s[j] != '$'))

    {

        if (st[i] == s[j])

        {

            i--;

            j++;
        }

        switch (st[i])

        {

        case 'e':
            s1 = 0;

            break;

        case 'b':
            s1 = 1;

            break;

        case 't':
            s1 = 2;

            break;

        case 'c':
            s1 = 3;

            break;

        case 'f':
            s1 = 4;

            break;
        }

        switch (s[j])

        {

        case 'i':
            s2 = 0;

            break;

        case '+':
            s2 = 1;

            break;

        case '*':
            s2 = 2;

            break;

        case '(':
            s2 = 3;

            break;

        case ')':
            s2 = 4;

            break;

        case '$':
            s2 = 5;

            break;
        }

        if (m[s1][s2][0] == '\0')

        {

            printf("\nERROR");

            exit(0);
        }

        else if (m[s1][s2][0] == 'n')

            i--;

        else if (m[s1][s2][0] == 'i')

            st[i] = 'i';

        else

        {

            for (k = s[s1][s2] - 1; k >= 0; k--)

            {

                st[i] = m[s1][s2][k];

                i++;
            }

            i--;
        }

        for (k = 0; k <= i; k++)

            printf(" %c", st[k]);

        printf("       ");

        for (k = j; k <= n; k++)

            printf("%c", s[k]);

        printf(" \n ");
    }

    printf("\n SUCCESS");
 return 0;
}