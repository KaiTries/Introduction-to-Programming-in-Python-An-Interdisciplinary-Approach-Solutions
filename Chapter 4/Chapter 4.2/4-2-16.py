#median function
import stdstats


def median(a):
    a.sort()
    if len(a)%2 == 1:
        return a[len(a)//2]
    else: return (a[(len(a)//2)-1] + a[len(a)//2]) / 2



