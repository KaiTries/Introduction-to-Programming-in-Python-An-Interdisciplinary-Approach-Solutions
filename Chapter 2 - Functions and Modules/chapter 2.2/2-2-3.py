import stdio
import stdrandom
import stdstats
import random

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


#stress-test:
a = [0,0,0,0,0,0]
stdio.write(stdrandom.discrete(a))
#result:
#None
#stress-test:
a = [0,0,0,0,0,-1]
stdio.write(stdrandom.discrete(a))
#result:
#0
#stress-test:
stdrandom.uniformInt(-1,0.5)
#ValueError: non-integer stop for randrange()

#etc, they behave as expected