import math
import stdarray

#transpose

a = [[99, 85, 98],[98, 57, 78],[92, 77, 76],[94, 32, 11],[99, 34, 22],[90, 46, 54],[76, 59, 88],[92, 66, 89],[97, 71, 24],[89, 29, 38]]
print (a)
b = []

for i in range(len(a[0])):
    t = []
    for j in range(len(a)):
        t += [a[j][i]]
    b += [t]

print (b)