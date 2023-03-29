#bitonic is firstly increasing then decreasing

#or do binary search with end condition:  i-1 < i > i + 1

a = [1,2,3,4,5,6,4,4,3,2,1]

def bitonicMax(a,start,end):
    l = start
    r = end
    if a[l] > a[l-1] and a[l] > a[l+1]: return l

    mid = (start+end) // 2
    if a[mid] > a[mid-1] and a[mid] < a[mid + 1]:
        return bitonicMax(a,mid+1,r)
    else:
        return bitonicMax(a,l,mid)
