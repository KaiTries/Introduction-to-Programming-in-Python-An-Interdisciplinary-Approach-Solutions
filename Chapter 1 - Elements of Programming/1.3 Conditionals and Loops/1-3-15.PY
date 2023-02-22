import sys
import stdio

n = int(sys.argv[1])

for i in range(1, n+1):
    #write the ith line of the table
    for j in range(1, n+1):
        #write the jth entry of the ith line
        if (i % j == 0) or (j % i == 0):
            stdio.write('*')
        else:
            stdio.write(' ')
    stdio.writeln(i)


p = 1

while p <= n:
    o = 1
    while o <= n:
        if (p % o == 0) or (o % p == 0):
            stdio.write('*')
            o += 1
        else:
            stdio.write(' ')
            o += 1
    stdio.writeln(p)
    p += 1