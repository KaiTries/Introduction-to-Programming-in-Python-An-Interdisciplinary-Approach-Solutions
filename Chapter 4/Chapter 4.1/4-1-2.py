#-----------------------------------------------------------------------
# threesum.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys
#-----------------------------------------------------------------------

# Write to standard output the triples in array a that sum to 0.

def writeTriples(a,x):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) == x:
                    stdio.writef('%d %d %d\n', a[i], a[j], a[k])

#-----------------------------------------------------------------------

# Return the number of triples in array a that sum to 0.

def countTriples(a,x):
    n = len(a)
    closest = 0
    current = 100
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if abs(((a[i] + a[j] + a[k]) - x)) < current:
                    current = abs(((a[i] + a[j] + a[k]) - x))
                    closest = (a[i] , a[j] , a[k])
    return closest

#-----------------------------------------------------------------------

# Read an array of integers from standard input. Write to standard
# output the count of triples in the array that that sum to 0. If
# the count is low, then also write the triples.

def main():
    x = int(sys.argv[1])
    a = stdarray.readInt1D()
    count = countTriples(a,x)
    print(count)
    writeTriples(a,x)


if __name__ == '__main__':
    main()


#-----------------------------------------------------------------------