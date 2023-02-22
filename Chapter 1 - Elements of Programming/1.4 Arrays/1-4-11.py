import math
import stdarray

#transpose
n = 3

a = stdarray.create2D(n,n,0)

print("original matrix is")
for i in range(n):
 for j in range(n):
  print(a[i][j], " ", end='')
 print()


for i in range(n):
    for j in range(i+1, n):
        a[i][j], a[j][i] = a[j][i], a[i][j]

print("Modified matrix is")
for i in range(n):
 for j in range(n):
  print(a[i][j], " ", end='')
 print()