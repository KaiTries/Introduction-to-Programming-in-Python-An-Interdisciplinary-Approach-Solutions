#f() monotonically increasing function a < 0 and b > 0 
#find x for which f(x) = 0



def func(x):
    return (x/2) + 3



def findX(a,b,err=0.001):
    fna = func(a)
    fnb = func(b)
    if fna > 0 or fnb < 0: return "f(a) !< 0 or f(b) !> 0"
    if abs(fna) == err: return a

    mid = (a + b) / 2
    if func(mid) > 0: return findX(a,mid)
    elif func(mid) < 0: return findX(mid,b)
    else: return mid


print(findX(-4,10))

