import random
import sys
import stdarray
import stdio
import stddraw
import stdrandom


moves = int(sys.argv[1])
n = stdio.readInt()
p = stdarray.readFloat2D()


page = 0      
hits = stdarray.create1D(n,0)

stddraw.setXscale(0,n)
stddraw.setYscale(0,n)

for i in range(moves): 
    page = stdrandom.discrete(p[page])                    
    hits[page] += 1                         
    if i % (moves/10) == 0:
        stddraw.clear()
        for k in range(n):
            stddraw.filledRectangle(k + 0.25, 0.0, 0.5, hits[k])
        stddraw.setYscale(0,max(hits)+moves)
        stddraw.show(100)


for v in hits:
    stdio.writef('%8.5f', 1.0 * v / moves)
stdio.writeln()

stddraw.show()
