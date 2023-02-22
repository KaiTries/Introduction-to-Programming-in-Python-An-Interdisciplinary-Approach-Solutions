import sys
import stdio

n = int(input("n:"))

factor = 2
while factor*factor <= n:
    if n % factor == 0:
        stdio.write(str(factor) + " ")
    while (n % factor) == 0:
        n //= factor
        #stdio.write(str(factor) + " ")
    factor += 1

if n > 1:
    stdio.write(n)
    stdio.writeln()    