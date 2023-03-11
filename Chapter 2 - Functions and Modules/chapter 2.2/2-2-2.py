import stdstats
import stdrandom
import sys
import stdio
import random
#both modules have test clients in them:


#stdstats:
def _main():
    """
    For testing:
    """
    import stdarray
    import stdio

    a = stdarray.readFloat1D()
    #stdio.writef('       min %7.3f\n', min(a))
    #stdio.writef('       max %7.3f\n', max(a))
    stdio.writef('      mean %7.3f\n', stdstats.mean(a))
    stdio.writef('   std dev %7.3f\n', stdstats.stddev(a))
    stdio.writef('    median %7.3f\n', stdstats.median(a))


#stdrandom

def _main():
    """
    For testing.
    """
    import sys
    import stdio
    stdrandom.seed(1)
    n = int(sys.argv[1])
    for i in range(n):
        stdio.writef(' %2d '   , stdrandom.uniformInt(10, 100))
        stdio.writef('%8.5f '  , stdrandom.uniformFloat(10.0, 99.0))
        stdio.writef('%5s '    , stdrandom.bernoulli())
        stdio.writef('%5s '    , stdrandom.binomial(100, .5))
        stdio.writef('%7.5f '  , stdrandom.gaussian(9.0, .2))
        stdio.writef('%2d '    , stdrandom.discrete([.5, .3, .1, .1]))
        stdio.writeln()


n = int(sys.argv[1])

for i in range(n):
    stdio.writeln(random.random())