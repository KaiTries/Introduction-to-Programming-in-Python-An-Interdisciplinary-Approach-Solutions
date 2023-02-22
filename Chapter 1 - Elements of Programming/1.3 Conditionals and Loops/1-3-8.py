#Generalizing the "uniform random number" exercise from section 1.2 (exercise 1.2.27) compose a program that accepts an integer n as a command line argument, uses random.random()
#to write n uniform random numbers between 0 and 1 and the nwrites their average value their minimum value and their maximum value.


#-----------------------------------------------------------------------
# stats1.py
#-----------------------------------------------------------------------

import stdio
import random
import sys

n = int(sys.argv[1])

min = 1.0
max = 0.0
sum = 0.0

for i in range(n):
    r = random.random()
    sum += r
    if r < min:
        min = r
    if r > max:
        max = r