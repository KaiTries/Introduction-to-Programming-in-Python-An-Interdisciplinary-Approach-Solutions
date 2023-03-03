import stdio
import sys
import math


n = int(sys.argv[1])
total = 0
a = []
b = []
for i in range(n):
    x = stdio.readFloat()
    a += [x]
    b += [x]
    total += x

mean = total / n

for i in range(n):
    b[i] -= mean

for i in range(n):
    b[i] = b[i]**2

summ = 0
for i in range(n):
    summ += b[i]

std = math.sqrt(summ)/n
stdio.write("the outliers are: ")
for i in range(n):
    if a[i] > ((1.5*std)+mean) or a[i] <(mean-(1.5*std)):
        stdio.write(str(a[i]) + " ")

stdio.writeln()
print("the mean is ", mean)
print("the standard deviation is ", std)

