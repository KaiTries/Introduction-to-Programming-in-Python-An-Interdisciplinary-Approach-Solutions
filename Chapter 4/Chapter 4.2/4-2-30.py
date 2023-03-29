#sort array with at most two diff values

a = [1,2,1,2,2,1,2,2,2,2,1,1,1,1,2,1]

def partitioning(a):
    l = 0
    r = len(a)-1
    big = 0
    for i in range(1,len(a)):
        if a[i] > a[i-1]:
            big = a[i]
            break
    print(big)
    
    while l < r:
        if a[l] < big:
            l += 1
        if a[r] == big:
            r -= 1
        elif a[l] > a[r]:
            a[l],a[r] = a[r],a[l]
            l += 1
            r -= 1
    return a

a = partitioning(a)
print(a)