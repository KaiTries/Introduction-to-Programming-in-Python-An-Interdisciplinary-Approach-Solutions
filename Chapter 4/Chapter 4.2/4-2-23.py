#furthest pair



def furthestpair(a):
    a.sort()
    return a[0],a[len(a)-1]