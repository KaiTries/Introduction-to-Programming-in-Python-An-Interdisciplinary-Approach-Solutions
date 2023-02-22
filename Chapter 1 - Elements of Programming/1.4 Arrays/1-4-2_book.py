import random
import stdarray
import stdio

n = int(input("Enter a number: "))

count = 0
collectedCount = 0
isCollected = stdarray.create1D(n, False)

while collectedCount < n:
    #generate another coupon
    value = random.randrange(0, n)
    count += 1
    if not isCollected[value]:
        collectedCount += 1
        isCollected[value] = True

stdio.writeln(count)