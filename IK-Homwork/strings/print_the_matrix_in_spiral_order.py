"""
Print the matrix in spiral order
Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

input mat[m][n] 2-d array

0,0  0,1  02 03 13 23 33 32 31 30 20 10 11 12 22 21

"""

def spiral_order_matrix(m):
   m = len(m)    #rows
   n = len(m[0]) #columns

   visited = set()

   i=0
   j=0
   row_boundary = m
   col_boundary = n
   while i < row_boundary and j < col_boundary:
       #print the first row from the remaining rows
       for i
       print m[i][j]
       while j < col_boundary:
            print m[i][j]
            j +=1
       i += 1
       col_boundary -= 1

   while (k < m & & l < n)
       {
       // Print
       the
       first
       row
       from the remaining
       rows
       for (i = l; i < n; ++i)
       {
       System.out.print(a[k][i]+" ");
       }
       k++;

       // Print the last column from the remaining columns
       for (i = k; i < m; ++i)
       {
       System.out.print(a[i][n-1]+" ");
       }
       n--;

       // Print the last row from the remaining rows * /
       if ( k < m)
       {
       for (i = n-1; i >= l; --i)
       {
       System.out.print(a[m-1][i]+" ");
       }
       m--;
       }

       // Print the first column from the remaining columns * /
       if (l < n)
       {
       for (i = m-1; i >= k; --i)
       {
       System.out.print(a[i][l]+" ");
       }
       l++;
       }
       }
   }



