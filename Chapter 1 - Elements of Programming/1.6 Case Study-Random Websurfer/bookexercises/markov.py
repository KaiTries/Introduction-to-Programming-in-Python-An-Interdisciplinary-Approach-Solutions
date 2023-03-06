import sys
import stdarray
import stdio
import stddraw

moves = int(sys.argv[1])
n = stdio.readInt()

p = stdarray.create2D(n,n,0.0)
for i in range(n):
    for j in range(n):
        p[i][j] = stdio.readFloat()


ranks = stdarray.create1D(n,0.0)
ranks[0] = 1.0

for i in range(moves):
    newRanks = stdarray.create1D(n,0.0)
    for j in range(n):
        for k in range(n):
            newRanks[j] += ranks[k] * p[k][j]
    ranks = newRanks


for i in range(n):
    stdio.writef('%8.5f', ranks[i])
stdio.writeln()


stddraw.setXscale(0,n)
stddraw.setYscale(0,max(ranks)+1)
stddraw.clear()
for k in range(n):
    stddraw.filledRectangle(k + 0.25, 0.0, 0.5, ranks[k])
stddraw.show()