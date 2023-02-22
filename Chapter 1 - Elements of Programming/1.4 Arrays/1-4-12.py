import math
import stdarray

#transpose

a = stdarray.create2D(3,3,0)
print (a)
b = []

for i in range(len(a[0])):
    t = []
    for j in range(len(a)):
        t += [a[j][i]]
    b += [t]

print (b)