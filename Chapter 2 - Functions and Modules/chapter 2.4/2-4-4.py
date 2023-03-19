#client of percolation like visualize 
#series of experiments with increasing p
import sys
import stddraw
import percolationv
import percolationio

#-----------------------------------------------------------------------

# Accept integer n, float p, and integer t as command-line arguments.
# Generate a n-by-n random system with site vacancy probability p.
# Compute the directed percolation flow, and draw result to standard
# draw. Repeat t times.

def main():
    trials = 10
    for j in range(trials):
        n = 10
        steps = 5
        diff = 1/steps
        p = 0
        for i in range(steps+1):
            isOpen = percolationio.random(n, i*diff)
            stddraw.clear()
            stddraw.setPenColor(stddraw.BLACK)
            percolationio.draw(isOpen, False)
            stddraw.setPenColor(stddraw.BLUE)
            full = percolationv.flow(isOpen)
            percolationio.draw(full, True)
            stddraw.show(1000.0)
    stddraw.show()


if __name__ == '__main__':main()