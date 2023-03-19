#modify bernoulli animate

import sys
import math
import stdarray
import stddraw
import stdrandom
import stdstats
import gaussian
import stdio
import percolation
import percolationio



#-----------------------------------------------------------------------
def evaluate(n, p, trials):
    count = 0
    for i in range(trials):
        # Generate one random network.
        isOpen = percolationio.random(n, p)
        if (percolation.percolates(isOpen)):
            count += 1
    return 1.0 * count / trials
#-----------------------------------------------------------------------

def bernoulliplot(n):
    norm = stdarray.create1D(n+1, 0.0)
    freq = stdarray.create1D(n+1, 0)
    stddraw.setCanvasSize(1000, 400)
    for t in range(trials):
        heads = stdrandom.binomial(n, 0.5)
        freq[heads] += 1
        for i in range(n+1):
            norm[i] = 1.0 * freq[i] / trials
            stdstats.plotBars(norm)
        stddraw.show(1)
    return 

def gaussplot(n):
    phi = stdarray.create1D(n+1, 0.0)
    stddev = math.sqrt(n)/2.0
    for i in range(n+1):
        phi[i] = gaussian.pdf(i, n/2.0, stddev)
    return stdstats.plotLines(phi)

#-----------------------------------------------------------------------

stdio.write("input n possibilites: ")
n = stdio.readInt()
stdio.write("input number of trials: ")
trials = stdio.readInt()

bernoulliplot(n)
gaussplot(n)
stddraw.show()