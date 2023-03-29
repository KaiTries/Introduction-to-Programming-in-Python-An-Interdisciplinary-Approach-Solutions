#quicksort


def partitioning(a,div):
    l = 0
    r = len(a)-1
    big = div
 
    while l < r:
        if a[l] < big:
            l += 1
        if a[r] >= big:
            r -= 1
        elif a[l] > a[r]:
            a[l],a[r] = a[r],a[l]
            l += 1
            r -= 1
    return a


def quicksort(a):
    
    div = a[len(a)-1]
    partitioning(a,div)



