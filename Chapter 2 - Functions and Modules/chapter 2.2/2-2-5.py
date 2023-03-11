import gaussian
import stdstats
import stddraw

#plot with fixed mean and different deviations

for i in range(5):
    sigma = i+1
    a = []
    x = -10
    while x < 10:
        y = gaussian.pdf(x,0,sigma)
        a += [y]
        x += 0.01
    stdstats.plotLines(a)

#plot with fixed deviation and different means
stddraw.setPenColor(stddraw.BLUE)

for i in range(5):
    m = -2+i
    a = []
    x = -10
    while x < 10:
        y = gaussian.pdf(x,m)
        a += [y]
        x += 0.01
    stdstats.plotLines(a)

stddraw.setPenColor(stddraw.CYAN)
a = []
x = -10
while x < 10:
    y = gaussian.pdf(x)
    a += [y]
    x += 0.01
stdstats.plotLines(a)

stddraw.show()