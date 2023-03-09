import random
import sys
import stdarray
import stdio
import stddraw


n = stdio.readInt()

p = stdarray.create2D(n,n,0.0)
for i in range(n):                          #loads the 2d matrix output into a 2d array
    for j in range(n):
        p[i][j] = stdio.readFloat()


hits = stdarray.create1D(n,0)
page = random.randint(0,n-1)                #starting point
count = 0

while sum(hits) < n:                      #how many times do we switch a page
    r = random.random()                     #gives randomness
    total = 0.0                             #counter 
    for j in range(0,n):                    #iterates through all the possibible paths from the current page
        total += p[page][j]                 #adds the value of the probability per path together
        if r < total:                       #if the values have exceeded the value given by randomnesss 
            page = j                        #we move to that page
            break
    if hits[page] == 0:
        hits[page] += 1                     #we count how many times we went to that page and repeat the loop
    count += 1

for v in hits:
    stdio.writef('%8.5f', 1.0 * v / count)
stdio.writeln()

stddraw.show()
