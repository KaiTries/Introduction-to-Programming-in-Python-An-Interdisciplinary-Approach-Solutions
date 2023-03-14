import stdstats
import stdio
import sys
import stddraw


def animatedgraph(m):
    nmbrs = stdio.readAllFloats()
    stddraw.setYscale(0,max(nmbrs)+100)
    for i in range(m,len(nmbrs)):
        stddraw.clear()
        num = []
        for j in range(m):
            num += [nmbrs[i-(m-j)]]
        stdstats.plotBars(num)
        stddraw.show(100)
    return stddraw.show()

m = int(sys.argv[1])
animatedgraph(m)