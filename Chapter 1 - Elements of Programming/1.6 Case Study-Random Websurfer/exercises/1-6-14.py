#generator for transition


import random
import sys
import stdio


n = int(sys.argv[1])
m = int(sys.argv[2])

#set how many hubs you want, they receive links from 10% off all website
h = int(sys.argv[3])
for i in range(h):
    i = random.randint(0,n-1)               #chose hub at random
    for j in range(int(n/10)):
        stdio.write(i)
        stdio.write(" ")
        stdio.write(random.randint(0,n-1))
        stdio.write(" ")
    stdio.writeln()




#set how many authorities you want, they have links to 10% off all website
a = int(sys.argv[4])
for i in range(a):
    i = random.randint(0,n-1)               #chose authority at random
    for j in range(int(n/10)):
        stdio.write(i)
        stdio.write(" ")
        stdio.write(random.randint(0,n-1))
        stdio.write(" ")
    stdio.writeln()






count = 0
stdio.writeln(n)
while count < m:
    stdio.write(random.randint(0,n-1))
    stdio.write(" ")
    stdio.write(random.randint(0,n-1))
    stdio.writeln()
    count += 1
