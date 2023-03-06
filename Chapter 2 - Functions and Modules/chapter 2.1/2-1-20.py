import random
import sys
import stdarray
import stdio

def getCoupon(n,rare):
    r = random.random()
    if r < (1/(1000*n)):
        x = rare
    else:
        x = random.randrange(0,n)
        while x == rare:
         x = random.randrange(0,n)           
    return x



def collect(n):
    hits = stdarray.create1D(n,0)
    isCollected = stdarray.create1D(n,0)
    count = 0
    collectedCount = 0
    while collectedCount < n:
        value = getCoupon(n,rare)
        count += 1
        hits[value] += 1
        if not isCollected[value]:
            collectedCount += 1
            isCollected[value] = True
    return count

n = int(sys.argv[1])
rare = random.randrange(0,n)
result = collect(n)
stdio.writeln(result)
stdio.writeln(rare)
