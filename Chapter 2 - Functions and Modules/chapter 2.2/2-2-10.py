#test client matrix multiplication markov
import matrix
import sys
import stdarray


moves = int(sys.argv[1])
p = stdarray.readFloat2D()

for i in range(moves):
    p = matrix.multiplyMM(p, p)
stdarray.write1D(p)