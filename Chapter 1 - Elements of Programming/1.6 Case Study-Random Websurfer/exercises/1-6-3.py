import stdarray
import stdio

n = stdio.readInt()

linkCounts = stdarray.create2D(n,n,0)
outDegrees = stdarray.create1D(n,0)

while not stdio.isEmpty():
    #accumulate link counts
    i = stdio.readInt()
    j = stdio.readInt()
    outDegrees[i] += 1
    linkCounts[i][j] += 1


stdio.writeln(int(n))

for i in range(n):
    #write probability distribution for row i.
    for j in range(n):
        #write probability for column j.
        if outDegrees[i] == 0:
            p = 1/n
        else:
            p = (0.90 * linkCounts[i][j] / outDegrees[i] + (0.10 / n))
        stdio.writef('%8.5f', p)
    stdio.writeln()

