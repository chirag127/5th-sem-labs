//  . Write program to find Simulate fir and fo of any given grammar.

// C program to calculate the fir and
// fo sets of a given grammar
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Functions to calculate fo
void ff(char, int, int);
void fo(char c);

// Function to calculate fir
void ffi(char, int, int);

int count, n = 0;

// Stores the final result
// of the fir Sets
char cfi[10][100];

// Stores the final result
// of the fo Sets
char cfo[10][100];
int m = 0;

// Stores the pro rules
char pro[10][10];
char f[10], fir[10];
int k;
char ck;
int e;

int main(int argc, char **argv)
{
  int jm = 0;
  int km = 0;
  int i, choice;
  char c, ch;
  count = 8;

  // The Input grammar
  strcpy(pro[0], "E=TR");
  strcpy(pro[1], "R=+TR");
  strcpy(pro[2], "R=#");
  strcpy(pro[3], "T=FY");
  strcpy(pro[4], "Y=*FY");
  strcpy(pro[5], "Y=#");
  strcpy(pro[6], "F=(E)");
  strcpy(pro[7], "F=i");

  int kay;
  char done[count];
  int ptr = -1;

  // Initializing the cfi array
  for (k = 0; k < count; k++)
  {
    for (kay = 0; kay < 100; kay++)
    {
      cfi[k][kay] = '!';
    }
  }
  int point1 = 0, point2, xxx;

  for (k = 0; k < count; k++)
  {
    c = pro[k][0];
    point2 = 0;
    xxx = 0;

    // Checking if fir of c has
    // already been calculated
    for (kay = 0; kay <= ptr; kay++)
      if (c == done[kay])
        xxx = 1;

    if (xxx == 1)
      continue;

    // Function call
    ffi(c, 0, 0);
    ptr += 1;

    // Adding c to the calculated list
    done[ptr] = c;
    printf("\n fir(%c) = { ", c);
    cfi[point1][point2++] = c;

    // Printing the fir Sets of the grammar
    for (i = 0 + jm; i < n; i++)
    {
      int lark = 0, chk = 0;

      for (lark = 0; lark < point2; lark++)
      {

        if (fir[i] == cfi[point1][lark])
        {
          chk = 1;
          break;
        }
      }
      if (chk == 0)
      {
        printf("%c, ", fir[i]);
        cfi[point1][point2++] = fir[i];
      }
    }
    printf("}\n");
    jm = n;
    point1++;
  }
  printf("\n");
  printf("-----------------------------------------------\n\n");
  char donee[count];
  ptr = -1;

  // Initializing the cfo array
  for (k = 0; k < count; k++)
  {
    for (kay = 0; kay < 100; kay++)
    {
      cfo[k][kay] = '!';
    }
  }
  point1 = 0;
  int land = 0;
  for (e = 0; e < count; e++)
  {
    ck = pro[e][0];
    point2 = 0;
    xxx = 0;

    // Checking if fo of ck
    // has already been calculated
    for (kay = 0; kay <= ptr; kay++)
      if (ck == donee[kay])
        xxx = 1;

    if (xxx == 1)
      continue;
    land += 1;

    // Function call
    fo(ck);
    ptr += 1;

    // Adding ck to the calculated list
    donee[ptr] = ck;
    printf(" fo(%c) = { ", ck);
    cfo[point1][point2++] = ck;

    // Printing the fo Sets of the grammar
    for (i = 0 + km; i < m; i++)
    {
      int lark = 0, chk = 0;
      for (lark = 0; lark < point2; lark++)
      {
        if (f[i] == cfo[point1][lark])
        {
          chk = 1;
          break;
        }
      }
      
      if (chk == 0)
      {
        printf("%c, ", f[i]);
        cfo[point1][point2++] = f[i];
      }
    }
    printf(" }\n\n");
    km = m;
    point1++;
  }
}

void fo(char c)
{
  int i, j;

  // Adding "$" to the fo
  // set of the start symbol
  if (pro[0][0] == c)
  {
    f[m++] = '$';
  }
  for (i = 0; i < 10; i++)
  {
    for (j = 2; j < 10; j++)
    {
      if (pro[i][j] == c)
      {
        if (pro[i][j + 1] != '\0')
        {
          // Calculate the fir of the next
          // Non-Terminal in the pro
          ff(pro[i][j + 1], i, (j + 2));
        }

        if (pro[i][j + 1] == '\0' && c != pro[i][0])
        {
          // Calculate the fo of the Non-Terminal
          // in the L.H.S. of the pro
          fo(pro[i][0]);
        }
      }
    }
  }
}

void ffi(char c, int q1, int q2)
{
  int j;

  // The case where we
  // encounter a Terminal
  if (!(isupper(c)))
  {
    fir[n++] = c;
  }
  for (j = 0; j < count; j++)
  {
    if (pro[j][0] == c)
    {
      if (pro[j][2] == '#')
      {
        if (pro[q1][q2] == '\0')
          fir[n++] = '#';
        else if (pro[q1][q2] != '\0' && (q1 != 0 || q2 != 0))
        {
          // Recursion to calculate fir of New
          // Non-Terminal we encounter after epsilon
          ffi(pro[q1][q2], q1, (q2 + 1));
        }
        else
          fir[n++] = '#';
      }
      else if (!isupper(pro[j][2]))
      {
        fir[n++] = pro[j][2];
      }
      else
      {
        // Recursion to calculate fir of
        // New Non-Terminal we encounter
        // at the beginning
        ffi(pro[j][2], j, 3);
      }
    }
  }
}

void ff(char c, int c1, int c2)
{
  int k;

  // The case where we encounter
  // a Terminal
  if (!(isupper(c)))
    f[m++] = c;
  else
  {
    int i = 0, j = 1;
    for (i = 0; i < count; i++)
    {
      if (cfi[i][0] == c)
        break;
    }

    // Including the fir set of the
    //  Non-Terminal in the fo of
    //  the original query
    while (cfi[i][j] != '!')
    {
      if (cfi[i][j] != '#')
      {
        f[m++] = cfi[i][j];
      }
      else
      {
        if (pro[c1][c2] == '\0')
        {
          // Case where we reach the
          // end of a pro
          fo(pro[c1][0]);
        }
        else
        {
          // Recursion to the next symbol
          // in case we encounter a "#"
          ff(pro[c1][c2], c1, c2 + 1);
        }
      }
      j++;
    }
  }
}
