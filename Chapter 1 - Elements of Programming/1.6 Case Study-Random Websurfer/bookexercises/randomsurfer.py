import random
import sys
import stdarray
import stdio
import stddraw



moves = int(sys.argv[1])

n = stdio.readInt()

p = stdarray.create2D(n,n,0.0)
for i in range(n):                          #loads the 2d matrix output into a 2d array
    for j in range(n):
        p[i][j] = stdio.readFloat()


hits = stdarray.create1D(n,0)
page = 0                                    #starting point

stddraw.setXscale(0,n)
stddraw.setYscale(0,n)

for i in range(moves):                      #how many times do we switch a page
    r = random.random()                     #gives randomness
    total = 0.0                             #counter 
    for j in range(0,n):                    #iterates through all the possibible paths from the current page
        total += p[page][j]                 #adds the value of the probability per path together
        if r < total:                       #if the values have exceeded the value given by randomnesss 
            page = j                        #we move to that page
            break
    hits[page] += 1                         #we count how many times we went to that page and repeat the loop
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
