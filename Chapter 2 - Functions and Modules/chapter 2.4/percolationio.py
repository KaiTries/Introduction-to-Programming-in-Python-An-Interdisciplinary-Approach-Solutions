import sys
import stdarray
import stddraw
import stdrandom

#-----------------------------------------------------------------------
def randomV(n, p=0.6):
    a = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    return a

# Return a random n-by-n matrix, each entry True with probability p.

def random(n,m=0, p=0.6):
    if m == 0:
        a = stdarray.create2D(n, n, False)
    else:
        a = stdarray.create2D(n, m, False)
    for i in range(n):
        for j in range(m):
            a[i][j] = stdrandom.bernoulli(p)
    return a

#-----------------------------------------------------------------------

# Draw system a to standard draw. Parameter which indicates whether
# to display the entries corresponding to True or to False.

def draw(a, which):
    n = len(a)
    m = len(a[1])
    stddraw.setXscale(-.5, n)
    stddraw.setYscale(-.5, n)
    for i in range(n):
        for j in range(m):
            if a[i][j] == which:
                stddraw.filledSquare(j, n-i-1, .5)

#-----------------------------------------------------------------------

# For testing.

def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    p = float(sys.argv[3])
    test = random(n,m, p)
    draw(test, False)
    stddraw.show()
    
if __name__ == '__main__':
    main()