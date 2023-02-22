import math
import random
n = int(input("length of the array: "))

a = []
for i in range(n):
    a += [random.random()]

print(a)

l = len(a)
for i in range(l // 2):
    temp = a[i]
    a[i] = a[l - i - 1]
    a[l - i - 1] = temp

print(a)
