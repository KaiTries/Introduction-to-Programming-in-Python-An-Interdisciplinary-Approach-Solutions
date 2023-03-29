#three variants


a = [1,2,1,2,2,1,3,2,2,2,1,3,3,1,2,1]

def partitioning(a):
    l = 0
    r = len(a)-1
    big = 0
    for i in range(1,len(a)):
        if a[i] > a[i-1]:
            big = a[i]
            break
 
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


#run particioning once and then split array and do again
def threevar(a):
    a = partitioning(a)
    start = 0
    for i in range(1,len(a)):
        if a[i] != a[i-1]:
            start = i
            break
    small_array = a[0:start]
    big_array = a[start:len(a)]
    big_array = partitioning(big_array)
    return small_array + big_array


print(threevar(a))