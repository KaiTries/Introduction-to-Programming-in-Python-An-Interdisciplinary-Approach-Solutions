#Random walkers. Suppose that n random walkers, starting in the center of an n-by-n grid, move one step at a time, choosing to go left, right, up, or down with equal probability at each step. 
#Compose a program to help formulate and test a hypothesis about the number of steps taken before all cells are touched.

#-----------------------------------------------------------------------
# randomwalkers.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys
import random

# Accept integer n as a command-line argument. Simulate how long it
# takes n random walkers starting at the center of an n-by-n grid to
# visit every cell in the grid. Write the number of steps to standard
# output.

n = int(input("number of runners in number-bynumber grid: "))

# Create arrays indicating the x and y positions of the walkers.
# All walkers begin at the middle of the grid.
x = stdarray.create1D(n, n//2)  # x positions
y = stdarray.create1D(n, n//2)  # y positions

cellsToVisit = n * n

# Create visited, an array that keeps track of which cells have
# been visited so far.
visited = stdarray.create2D(n, n, False) # has (i,j) been visited?
visited[n//2][n//2] = True
cellsToVisit -= 1

# Run the simulation.
steps = 0
while cellsToVisit > 0:
    steps += 1
    for i in range(n):
        # Move random walker i.
        r = random.randrange(0, 4)
        if r == 0:
            x[i] += 1
        elif r == 1:
            x[i] -= 1
        elif r == 2:
            y[i] += 1
        else:
            y[i] -= 1
        # Check if (x[i], y[i]) is inside the n-by-n boundary and
        # has been visited.
        if (x[i] < n) and (y[i] < n) and (x[i] >= 0) and (y[i] >= 0) \
            and not visited[x[i]][y[i]]:
            cellsToVisit -= 1
            visited[x[i]][y[i]] = True

stdio.writeln(steps)
