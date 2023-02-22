import stdarray
import stdio
import random

n = int(input("Enter the number of rows in the first matrix: "))
m = int(input("Enter the number of columns in the first matrix: "))
a = stdarray.create2D(n,m,0)

for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(0,9)

for i in range(n):
    for j in range(m):
        stdio.write(str(a[i][j]) + " ")
    stdio.writeln()

s = int(input("Enter the number of rows in the second matrix: "))
t = int(input("Enter the number of columns in the second matrix: "))
b = stdarray.create2D(s,t,0)

for i in range(s):
    for j in range(t):
        b[i][j] = random.randint(0,9)

for i in range(s):
    for j in range(t):
        stdio.write(str(b[i][j]) + " ")
    stdio.writeln()



if len(a[0]) == len(b):
    c = stdarray.create2D(len(a),len(b[0]),0)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    for i in range(len(c)):
        for j in range(len(c[i])):
            stdio.write(str(c[i][j]) + " ")
        stdio.writeln()
else:
    stdio.writeln("Cannot multiply these matrices")