import math
import stdarray
import stdio
import sys


a = []

while not stdio.isEmpty():
    x = stdio.readLine()
    x = x.split()
    for i in range(len(x)):
        x[i] = int(x[i])
    a += [x]

print (a)
peaks = 0
for i in range(1,len(a)-1):
    for j in range(1,min(len(a[i-1]),len(a[i]),len(a[i+1]))-1):
        if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]:
            peaks += 1


print(peaks)