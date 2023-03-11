#modify bernoulli animate

import sys
import math
import stdarray
import stddraw
import stdrandom
import stdstats
import gaussian
import stdio

#-----------------------------------------------------------------------

def bernoulliplot(n,p):
    norm = stdarray.create1D(n+1, 0.0)
    freq = stdarray.create1D(n+1, 0)
    stddraw.setCanvasSize(1000, 400)
    for t in range(trials):
        heads = stdrandom.binomial(n,p)
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
stdio.write("input p probability(0-1): ")
p = stdio.readFloat()
stdio.write("input number of trials: ")
trials = stdio.readInt()

bernoulliplot(n,p)
gaussplot(n)
stddraw.show()
