
#-----------------------------------------------------------------------
import estimate
# Return x such that Phi(x) = y.

def _evalInverse(n,p, delta,lo,hi):
    mid = lo + ((hi - lo) / 2.0)
    if (hi - lo) < delta:
        return mid
    if estimate.evaluate(n,n,mid,1000) > (p):
        return _evalInverse(n,p, delta, lo, mid)
    else:
        return _evalInverse(n,p, delta, mid, hi)
    
def evalInverse(n,p):
    return _evalInverse(n,p, 0.0001, 0, 1)
n = 10
p = 0.5
print(evalInverse(n,p))
p = 0.58
print(estimate.evaluate(n,n,p,1000))