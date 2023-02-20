#Compose a program that, using one for loop and one if statement, writes the integers from 1000 (inclusive) to 2000 (exclusive) with five integers per line. Hint: use the % operator.
import math
import sys
import stdio



for i in range(1000, 2000):
    if i % 5 == 0:
        stdio.writeln(i)
    else:
        stdio.write(str(i) + " ")