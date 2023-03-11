#test client
import matrix
import sys
import stdarray


moves = int(sys.argv[1])
p = stdarray.readFloat2D()



ranks = stdarray.create1D(len(p), 0.0)
ranks[0] = 1.0
for i in range(moves):
    ranks = matrix.multiplyVM(ranks, p)
stdarray.write1D(ranks)