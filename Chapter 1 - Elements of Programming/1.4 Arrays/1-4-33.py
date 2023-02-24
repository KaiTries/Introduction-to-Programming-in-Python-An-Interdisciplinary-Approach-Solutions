#Three-dimensional self-avoiding walks. 
#Run experiments to verify that the dead-end probability is 0 for a three-dimensional self-avoiding walk and to compute the average walk length for various values of n.

import random
import stdarray
import stdio

n = int(input("Size of the lattice: "))
trials = int(input("Number of trials: "))
deadEnds = 0
escape = 0
walkLength = 0




for t in range(trials):
    a = stdarray.create2D(n, n, False)
    b = [[[False for k in range(n)] for j in range(n)] for i in range(n)]
    x = n // 2
    y = n // 2
    z = n // 2
    while (x > 0) and (x < n - 1) and (y > 0) and (y < n - 1) and (z > 0) and (z < n - 1):
        b[x][y][z] = True
        if b[x + 1][y][z] and b[x - 1][y][z] and b[x][y + 1][z] and b[x][y - 1][z] and b[x][y][z + 1] and b[x][y][z - 1]:
            deadEnds += 1
            break
        r = random.randrange(1, 7)
        if (r == 1) and (not b[x + 1][y][z]): x += 1
        elif (r == 2) and (not b[x - 1][y][z]): x -= 1
        elif (r == 3) and (not b[x][y + 1][z]): y += 1
        elif (r == 4) and (not b[x][y - 1][z]): y -= 1
        elif (r == 5) and (not b[x][y][z + 1]): z += 1
        elif (r == 6) and (not b[x][y][z - 1]): z -= 1
        walkLength += 1
    if (x == 0) or (x == n - 1) or (y == 0) or (y == n - 1) or (z == 0) or (z == n - 1):
        escape += 1

stdio.writeln(str(100 * escape / trials) + "% escaped")
stdio.writeln(str(100 * deadEnds / trials) + "% dead ends")    
stdio.writeln(str(walkLength / trials) + " average walk length")


#For larger values of n, the dead end probability will go back to 1.
#The hypothesis in the book cannot be proven.