// Implement Intermediate code generation for simple expressions.

#include <stdio.h>
#include <string.h>
char op[2], arg1[5], arg2[5], r[5];
int main()
{
  FILE *fp1, *fp2;
  fp1 = fopen("input.txt", "r");
  fp2 = fopen("output.txt", "w");
  while (!feof(fp1))
  {

    fscanf(fp1, "%s%s%s%s", op, arg1, arg2, r);
    if (strcmp(op, "+") == 0)
    {
      fprintf(fp2, "\nMOV R0,%s", arg1);
      fprintf(fp2, "\nADD R0,%s", arg2);
      fprintf(fp2, "\nMOV %s,R0", r);
    }
    if (strcmp(op, "*") == 0)
    {
      fprintf(fp2, "\nMOV R0,%s", arg1);
      fprintf(fp2, "\nMUL R0,%s", arg2);
      fprintf(fp2, "\nMOV %s,R0", r);
    }
    if (strcmp(op, "-") == 0)
    {
      fprintf(fp2, "\nMOV R0,%s", arg1);
      fprintf(fp2, "\nSUB R0,%s", arg2);
      fprintf(fp2, "\nMOV %s,R0", r);
    }
    if (strcmp(op, "/") == 0)
    {
      fprintf(fp2, "\nMOV R0,%s", arg1);
      fprintf(fp2, "\nDIV R0,%s", arg2);
      fprintf(fp2, "\nMOV %s,R0", r);
    }
    if (strcmp(op, "=") == 0)
    {
      fprintf(fp2, "\nMOV R0,%s", arg1);
      fprintf(fp2, "\nMOV %s,R0", r);
    }
  }
  fclose(fp1);
  fclose(fp2);
  return 0;
}
