#dynamic histogram

import stdarray
import stdio
import stdstats
import stddraw
import sys

#---functions

def steps(l,r,n):                   #gives us boxes for floats to fall into
    a = stdarray.create1D(n,0)
    step = ((r-l)/n)
    for i in range(1,n+1):
        a[i-1] = l + (step*i)
    return a

def sortr(f,a,c):                   #sorts digit into box 
    for i in range(len(a)):
        if a[i] > f:
            c[i] += 1
            break
    return c

def intake(l,r,n):                  #reads float from command line and will sort them into boxes and display it in a bar graph
    a = steps(l,r,n)
    x = stdio.readAllFloats()
    c = stdarray.create1D(len(a),0)
    for i in range(len(x)):
        sortr(x[i],a,c)
    stddraw.setYscale(0,max(c)+1)
    stdstats.plotBars(c)
    return stddraw.show()

#--global code

n = int(sys.argv[1])
l = float(sys.argv[2])
r = float(sys.argv[3])

intake(l,r,n)

