#-----------------------------------------------------------------------
# threesum.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import random
#-----------------------------------------------------------------------

# Write to standard output the triples in array a that sum to 0.

def writeQuadruples(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for t in range(k+1,n):
                    if (a[i] + a[j] + a[k] + a[t]) == 0:
                        stdio.writef('%d %d %d %d\n', a[i], a[j], a[k],a[t])

#-----------------------------------------------------------------------

# Return the number of triples in array a that sum to 0.

def countQuadruples(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                    if (a[i] + a[j] + a[k]) == 0:
                        count += 1
    return count

#-----------------------------------------------------------------------

# Read an array of integers from standard input. Write to standard
# output the count of triples in the array that that sum to 0. If
# the count is low, then also write the triples.

def main():
    n = 100
    a = stdarray.create1D(n,0)
    for i in range(n):
        a[i] = random.randint(-2**32,2**32)

    count = countQuadruples(a)
    stdio.writeln(count)
    if count < 10:
        writeQuadruples(a)

if __name__ == '__main__':
    main()
