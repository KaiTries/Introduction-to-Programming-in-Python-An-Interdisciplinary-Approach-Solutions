#percolationd test only directed percolation
#percplot adjusted to draw a plot of directed percolation probability:
import stdarray
import percolationio
import percplot
import percolation
import stddraw


def main():
    n = 5
    stddraw.setPenRadius(0.0)
    percplot.curveD(n, 0.0, 0.0, 1.0, 1.0)
    stddraw.show()

main()