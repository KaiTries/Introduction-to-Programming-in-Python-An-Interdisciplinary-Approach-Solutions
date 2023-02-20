#Compose a program that takes two positive integers as command-line arguments and writes True if either evenly divides the other.

import sys
import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])

stdio.writeln(a % b == 0 or b % a == 0)

