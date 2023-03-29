#search in bitonic array

a = [0,2,3,4,5,6,4,4,3,2,1]

#find peak if ele higher than peak return -1 if ele lower than a[0] and a[len(a) - 1] also return -1
#use the peakfinder from last exercise

def binarysearch(a,x,lo,hi):
    if a[lo] == x: return True
    if hi <= lo: return False
    mid = (lo + hi) // 2
    if a[mid] >= x: return binarysearch(a,x,lo,mid)
    else: return binarysearch(a,x,mid+1,hi)

def bitonicMax(a,start,end):
    l = start
    r = end
    if a[l] > a[l-1] and a[l] > a[l+1]: return l

    mid = (start+end) // 2
    if a[mid] > a[mid-1] and a[mid] < a[mid + 1]:
        return bitonicMax(a,mid+1,r)
    else:
        return bitonicMax(a,l,mid)
    

def bitonicSearch(a,x):
    peak = bitonicMax(a,0,len(a))
    #seperate two halves
    first_half = a[0:peak+1]
    #second half we 
    second_half = a[peak+1:len(a)]
    second_half = second_half[::-1]
    #now do binary search on both of them
    fx = binarysearch(first_half,x,0,len(first_half))
    sx = binarysearch(second_half,x,0,len(second_half))
    #question only asks if it is in the array not which position so we can just answer like this
    return fx,sx

print(bitonicSearch(a,1))