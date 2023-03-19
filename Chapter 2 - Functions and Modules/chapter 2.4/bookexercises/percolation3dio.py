import sys
import stdarray
import stddraw
import stdrandom

#-----------------------------------------------------------------------
# Return a random n-by-n-by-n matrix, each entry True with probability p.
def random(n, p=0.5):
    z = stdarray.create1D(n,False)
    for t in range(n):
        a = stdarray.create2D(n, n, False)
        for i in range(n):
            for j in range(n):
                a[i][j] = stdrandom.bernoulli(p)
        z[t] = a
    return z

#-----------------------------------------------------------------------

