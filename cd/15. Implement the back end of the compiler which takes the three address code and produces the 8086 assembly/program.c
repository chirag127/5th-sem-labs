// Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language insuctions that can be assembled and run using an 8086 assembler. The target assembly insuctions can be simple move, add, sub, jump etc.

#include <stdio.h>

#include <string.h>

void main()
{
    char icode[10][30], s[20], o[10];
    int i = 0;
    // clrscr();
    printf("\n Enter intermediate code:\n");
    do
    {
        scanf("%s", icode[i]);
    } while (strcmp(icode[i++], "exit") != 0);
    printf("\n target code generation");
    i = 0;
    do
    {
        strcpy(s, icode[i]);
        switch (s[3])
        {
        case '+':
            strcpy(o, "ADD ");
            break;
        case '-':
            strcpy(o, "SUB ");
            break;
        case '*':
            strcpy(o, "MUL ");
            break;
        case '/':
            strcpy(o, "DIV ");
            break;
        }
        printf("\n\tMov %c,R%d", s[2], i);
        printf("\n\t%s%c,R%d", o, s[4], i);
        printf("\n\tMov R%d,%c", i, s[0]);
    } while (strcmp(icode[++i], "exit") != 0);
    // getch();
}
