#Compose a program that takes three positive integers as command-line arguments and writes False if any one of them is greater than or equal to the sum of the other two and True otherwise. 
#(Note: This computation tests whether the three numbers could be the lengths of the sides of some triangle.)

import sys
import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

stdio.writeln(a < b + c and b < a + c and c < a + b)