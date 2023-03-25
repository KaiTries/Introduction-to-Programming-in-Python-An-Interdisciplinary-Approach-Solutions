#histogram with counter
#-----------------------------------------------------------------------
# histogram.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
import stdrandom
import stdstats
from counter import Counter
#-----------------------------------------------------------------------

class Histogram:

    # Construct self such that it can store n frequency counts.
    def __init__(self, n):
        # Frequency counts.
        self._freqCounts = []
        for i in range(n):
            x = Counter(i,n)
            self._freqCounts += [x]

    # Add one occurrence of the value i to self.
    def addDataPoint(self, i):
        self._freqCounts[i].increment()

    # Draw self.
    def draw(self):
        stddraw.setYscale(0, max(self._freqCounts))
        stdstats.plotBars(self._freqCounts,0.5)

#-----------------------------------------------------------------------

# Accept integer n, float p, and integer trialCount as command-line
# arguments. Perform trialCount experiments, each of which counts the
# number of heads found when a biased coin (heads with probability p
# and tails with probability 1 - p) is flipped n times. Then, draw
# the results to standard draw.

def main():
    n = 10  # number of biased coin flips per trial
    p = 0.5  # heads with probability p
    trialCount = 100  # number of trials
    histogram = Histogram(n + 1)
    for trial in range(trialCount):
        heads = stdrandom.binomial(n, p)
        histogram.addDataPoint(heads)
  
    stddraw.setCanvasSize(500, 200)
    stddraw.clear(stddraw.LIGHT_GRAY)
    histogram.draw()
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------