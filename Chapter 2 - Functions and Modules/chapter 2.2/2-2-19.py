#compose a programm that uses matrix multiplication



import matrix
import sys
import stdarray
import stdrandom
import stddraw

def main():
    n = int(sys.argv[1])
    dist = stdarray.readFloat1D()
    cx = stdarray.readFloat2D()
    cy = stdarray.readFloat2D()
    x = 0.0
    y = 0.0
    stddraw.setPenRadius(0.0)
    for i in range(n):
        r = stdrandom.discrete(dist)
        x0 = matrix.multiplyMV(cx,r)
        y0 = matrix.multiplyMV(cy,r)
        x = x0
        y = y0
        stddraw.point(x, y)
    stddraw.show()

if __name__ == '__main__':
    main()

