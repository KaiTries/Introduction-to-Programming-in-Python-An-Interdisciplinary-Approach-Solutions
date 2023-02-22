#Minima in permutations. Compose a program that takes an integer n from the command line, generates a random permutation, writes the permutation, 
#and writes the number of left-to-right minima in the permutation (the number of times an element is the smallest seen so far). 
#Then compose a program that takes integers m and n from the command line, generates m random permutations of size n, and writes the average number 
#of left-to-right minima in the permutations generated. 
#Extra credit: Formulate a hypothesis about the number of left-to-right minima in a permutation of size n, as a function of n.

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

minima = 0 #initialize the minima

for i in range(len(list_n)): #count the minima
    if list_n[i] < list_n[i-1]: 
        minima += 1 

print(minima) #print the minima

m = int(input("Write the number of permutations here: ")) #input the number of permutations here
b = int(input("Write the size of the permutations here: ")) #input the size of the permutations here

minima = 0 #initialize the minima

for i in range(m): #generate m random permutations of size b
    list_b = stdarray.create1D(b, 0)
    for j in range(b):
        list_b[j] = j
    for j in range(b):
        r = random.randint(0, 9)
        list_b[j] = r
    print(list_b)

    for i in range(len(list_b)): #count the minima
        if list_b[i] < list_b[i-1]:
            minima += 1


print("The average number of minima is: ", minima/m) #print the average number of minima