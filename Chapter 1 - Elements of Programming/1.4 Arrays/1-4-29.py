#Find a duplicate. Given an array of n elements with each element between 1 and n, compose a code fragment to determine whether there are any duplicates. 
#You do not need to preserve the contents of the given array, but do not use an extra array.

import stdio
import stdarray
import sys
import random

n = int(input("enter the number of elements: "))

a = stdarray.create1D(n, 0)

for i in range(n):
    a[i] = random.randint(1, n)

stdio.writeln(a)

for i in range(n):
    for j in range(i+1, n):
        if a[i] == a[j]:
            print("There are duplicates of", a[i])
            break

