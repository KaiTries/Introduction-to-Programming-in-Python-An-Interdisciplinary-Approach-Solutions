import sys
import stdarray
import stdio
import stddraw

moves = int(sys.argv[1])
n = stdio.readInt()

p = stdarray.create2D(n,n,0.0)
for i in range(n):
    for j in range(n):
        p[i][j] = stdio.readFloat()


p_squared = stdarray.create2D(n,n,0.0)
p2 = p
for t in range(moves):
    p_squared = stdarray.create2D(n,n,0.0)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                p_squared[i][j] += p[i][k] * p[k][j]    
    p2 = p_squared

for i in range(n):
    #write probability distribution for row i.
    for j in range(n):
        #write probability for column j.
        stdio.writef('%15.5f', p_squared[i][j])
    stdio.writeln()
stdio.writeln()


