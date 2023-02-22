#inverse permutation. read permutation from integers 0 to n-1 from n lines of input and write inverse permutation to n lines of output.
#if an array is a[] then its inverse is the array b[] such that a[b[i]] = b[a[i]] = i.

import sys
import random
import math
import stdarray

n = int(input("Write the number here: ")) #input your number here

print(n) #print the number

list_n = [int(i) for i in str(n)] #convert the number to an array

print(list_n) #print the array

for i in range(len(list_n)):  # shuffle the array
    r = random.randrange(i, len(list_n))
    list_n[i], list_n[r] = list_n[r], list_n[i]

print(list_n) # print the array


b = stdarray.create1D(len(list_n), 0) #create an array of the same size as the original array

for i in range(len(list_n)): #create the inverse permutation
    b[i] = list_n[len(list_n)-1-i] #the last element of the original array is the first element of the inverse permutation and so on. the last one is len(list_n)-1.

print(b)