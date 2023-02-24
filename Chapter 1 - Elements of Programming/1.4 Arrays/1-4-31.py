#Minesweeper. Compose a program that takes three command-line arguments m, n, and p and produces an m-by-n boolean array where each element is occupied with probability p. 
#In the minesweeper game, occupied cells represent bombs and empty cells represent safe cells. Write the array using an asterisk for bombs and a period for safe cells. 
#Then, replace each safe square with the number of neighboring bombs (above, below, left, right, or diagonal) and write the result, as in this example.


import stdio
import stdarray
import sys
import random


m = int(input("enter the number of rows: "))
n = int(input("enter the number of columns: "))
p = float(input("enter the probability of a cell being occupied: "))

#create the matrix with m+2 rows and n+2 columns.

a = stdarray.create2D(m+2, n+2, False)

#initialize matrix with bombs and safe cells, with probability p. bombs = True and safe cells = False.

for i in range(m):
    for j in range(n):
        if random.random() < p:
            a[i][j] = True
        else:
            a[i][j] = False


#count the number of bombs in the neighboring cells.

for i in range(m):
    for j in range(n):
        if a[i][j] == False:
            count = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if a[k][l] == True:
                        count += 1
            a[i][j] = count

#write the matrix with bombs and safe cells.

for i in range(m):
    for j in range(n):
        if a[i][j] == True:
            stdio.write('* ')
        else:
            stdio.write(str(a[i][j]) + ' ')
    stdio.writeln()