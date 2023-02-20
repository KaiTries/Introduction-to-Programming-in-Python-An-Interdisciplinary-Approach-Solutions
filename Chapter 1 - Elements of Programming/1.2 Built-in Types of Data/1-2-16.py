#Compose a program that takes two integers a and b from the command line and writes a random integer between a and b.

import sys
import stdio
import random

a = int(sys.argv[1])
b = int(sys.argv[2])

print(a + random.randint(a,b) + b) 