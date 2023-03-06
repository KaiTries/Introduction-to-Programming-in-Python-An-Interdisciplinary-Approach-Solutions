#generator for transition


import random
import sys
import stdio


n = int(sys.argv[1])
m = int(sys.argv[2])

count = 0
stdio.writeln(n)
while count < m:
    stdio.write(random.randint(0,n-1))
    stdio.write(" ")
    stdio.write(random.randint(0,n-1))
    stdio.writeln()
    count += 1
