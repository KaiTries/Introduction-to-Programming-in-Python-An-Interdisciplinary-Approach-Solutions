import stdio
import sys
import math


n = int(sys.argv[1])
a = []
sol = []
for i in range(1,n+1):
    sol += [i]

for i in range(n-1):
    x = stdio.readInt()
    if x >= 1 and x <= n:
        if x not in a:
            a += [x]


missing = sum(sol) - sum(a)
stdio.write("missing number is: " + str(missing))