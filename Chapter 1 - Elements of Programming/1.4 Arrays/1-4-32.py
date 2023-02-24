#Self-avoiding walk length. Suppose that there is no limit on the size of the grid. Run experiments to estimate the average walk length.
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
    x = n // 2
    y = n // 2
    while (x > 0) and (x < n - 1) and (y > 0) and (y < n - 1):
        a[x][y] = True
        if a[x + 1][y] and a[x - 1][y] and a[x][y + 1] and a[x][y - 1]:
            deadEnds += 1
            break
        r = random.randrange(1, 5)
        if (r == 1) and (not a[x + 1][y]): x += 1
        elif (r == 2) and (not a[x - 1][y]): x -= 1
        elif (r == 3) and (not a[x][y + 1]): y += 1
        elif (r == 4) and (not a[x][y - 1]): y -= 1
        walkLength += 1
    if (x == 0) or (x == n - 1) or (y == 0) or (y == n - 1):
        escape += 1

stdio.writeln(str(100 * escape / trials) + "% escaped")
stdio.writeln(str(100 * deadEnds / trials) + "% dead ends")    
stdio.writeln(str(walkLength / trials) + " average walk length")

#Size of the lattice: 150
#Number of trials: 10000
#0.01% escaped
#99.99% dead ends
#115.4032 average walk length