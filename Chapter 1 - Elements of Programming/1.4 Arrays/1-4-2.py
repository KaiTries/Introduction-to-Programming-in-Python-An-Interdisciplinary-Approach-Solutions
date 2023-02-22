import math
import random
import stdarray


n = int(input("length of the array: "))

a = []
for i in range(n):
    a += [random.randint(0, 100)]
b = []
for i in range(n):
    b += [random.randint(0, 100)]
print(a)
print(b)
sqrs = 0
for i in range (n):
    sqrs += (a[i] - b[i]) ** 2

euc_dist = math.sqrt(sqrs)
print(euc_dist)