import stdio
import sys
import math


n = int(sys.argv[1])
total = 0
a = []
for i in range(n):
    x = stdio.readFloat()
    a += [x]
    total += x

mean = total / n

for i in range(n):
    a[i] -= mean

for i in range(n):
    a[i] = a[i]**2

summ = 0
for i in range(n):
    summ += a[i]

print("the mean is ", mean)
print("the standard deviation is ", (math.sqrt(summ)/n))
