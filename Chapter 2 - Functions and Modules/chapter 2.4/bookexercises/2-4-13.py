#vertical percolation
import estimatev
#math prob:

def mathProb(n,p):
    return 1-(1-p**n)**n


n = 10
p = 0.6

print(mathProb(n,p))

print(estimatev.evaluate(n,p,1000))