import math
import random
import stdarray
import stdio


n = int(input("number of rows "))
m = int(input("number of columns: "))

a = []
for i in range(n):
    i = []
    for j in range(m):
        val = random.randint(0,1)
        i += [bool(val)]
    a += [i]


print(a)

for i in range(n+1):
    if i == 0:
        stdio.write("  ")
    else:
        stdio.write(i)
    for j in range(m):
        if i == 0:
            stdio.write(str(j+1) + " ")
        else:
            if a[i-1][j] == True:
                stdio.write(" *")
            else:
                stdio.write("  ")
    stdio.writeln()

