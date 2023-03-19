
import sys
import stdio
import percolation
import percolationio
import percolation3dio
import percolation3d
#-----------------------------------------------------------------------

# Generate a random n-by-n system with site vacancy probability p
# and determine if the system percolates. Repeat t times. Return
# an estimate of the empirical percolation probability of such systems.

def evaluate(n,m, p, trials):
    count = 0
    for i in range(trials):
        # Generate one random network.
        isOpen = percolationio.random(n,m, p)
        if (percolation.percolates(isOpen)):
            count += 1
    return 1.0 * count / trials
#-----------------------------------------------------------------------
def evaluateD(n,m, p, trials):
    count = 0
    for i in range(trials):
        # Generate one random network.
        isOpen = percolationio.random(n,m, p)
        if (percolation.percolatesD(isOpen)):
            count += 1
    return 1.0 * count / trials
#-----------------------------------------------------------------------
def evaluateFast(n,m, p, trials):
    count = 0
    for i in range(trials):
        # Generate one random network.
        isOpen = percolationio.random(n,m, p)
        if (percolation.percolatesFast(isOpen)):
            count += 1
    return 1.0 * count / trials
#-----------------------------------------------------------------------
def evaluate3D(n, p, trials):
    count = 0
    for i in range(trials):
        # Generate one random network.
        isOpen = percolation3dio.random(n, p)
        if (percolation3d.percolates3D(isOpen)):
            count += 1
    return 1.0 * count / trials
#-----------------------------------------------------------------------
# Accept integer n, float p, and integer trials as command-line
# arguments. Create trials random n-by-n systems with site vacancy
# probability p. Determine the fraction of them that percolate, and
# write that fraction to standard output.

def main():
    n = int(sys.argv[1])
    m = float(sys.argv[2])
    p = float(sys.argv[3])
    trials = int(sys.argv[4])
    q = evaluate(n, p,m, trials)
    stdio.writeln(q)

if __name__ == '__main__':
    main()
    