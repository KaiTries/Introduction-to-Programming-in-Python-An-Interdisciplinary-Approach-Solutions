import sys
import math
import stdio

n = int(input('Enter a number: '))
k = int(input('Enter the base (between 2 and 16): '))

#while n > 0:
#    stdio.writeln(n % k)
#    n = n // k


#compute v as the largest power of k <= n
v = 1
while v <= n/k:
    v = v * k

print(2%3)
print(v)
#cast out powers of n in decreasing order
while v > 0:
    if (n // v) < 10:
        stdio.write(n // v)
    elif (n // v) == 10:
        stdio.write('A')
    elif (n // v) == 11:
        stdio.write('B')
    elif (n // v) == 12:
        stdio.write('C')
    elif (n // v) == 13:
        stdio.write('D')
    elif (n // v) == 14:
        stdio.write('E')
    elif (n // v) == 15:
        stdio.write('F')
    n = n % v
    v = v // k


