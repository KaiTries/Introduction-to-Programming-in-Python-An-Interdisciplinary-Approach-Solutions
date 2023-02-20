#Write a code fragment that takes two float command-line arguments, and writes True if both are strictly between 0 and 1 and False otherwise.

import sys

#input

a = float(sys.argv[1])
b = float(sys.argv[2])

#process

if a > 0 and a < 1 and b > 0 and b < 1:
    print ("True")
else:
    print ("False")