#sicherman dice
import stdrandom
import stdstats
import stdarray
import stddraw

d1 = [1,3,4,5,6,8]
d2 = [1,2,2,3,3,4]

sums = stdarray.create1D(13,0)  #sums up to twelve

for i in range(1000):
    r1 = stdrandom.uniformInt(0,6)
    r2 = stdrandom.uniformInt(0,6)
    x = d1[r1] + d2[r2]
    sums[x] += 1

print(sums)
stddraw.setYscale(0,max(sums)+5)
stdstats.plotBars(sums)

d1 = [1,2,3,4,5,6]
d2 = [1,2,3,4,5,6]

sums = stdarray.create1D(13,0)  #sums up to twelve

for i in range(1000):
    r1 = stdrandom.uniformInt(0,6)
    r2 = stdrandom.uniformInt(0,6)
    x = d1[r1] + d2[r2]
    sums[x] += 1

print(sums)
stddraw.setYscale(0,max(sums)+5)
stddraw.setPenColor(stddraw.BLUE)
stdstats.plotBars(sums)
stddraw.show()