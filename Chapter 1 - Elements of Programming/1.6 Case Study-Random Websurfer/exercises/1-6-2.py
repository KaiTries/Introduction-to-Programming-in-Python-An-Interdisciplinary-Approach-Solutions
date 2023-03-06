import stdarray
import stdio
import sys


leap = float(sys.argv[1])

n = stdio.readInt()

linkCounts = stdarray.create2D(n,n,0)
outDegrees = stdarray.create1D(n,0)

while not stdio.isEmpty():
    #accumulate link counts
    i = stdio.readInt()
    j = stdio.readInt()

    if linkCounts[i][j] == 0:
        linkCounts[i][j] += 1
        outDegrees[i] += 1


stdio.writeln(int(n))

for i in range(n):
    #write probability distribution for row i.
    for j in range(n):
        #write probability for column j.
        p = ((1-leap) * linkCounts[i][j] / outDegrees[i] + (leap / n))
        stdio.writef('%8.5f', p)
    stdio.writeln()

