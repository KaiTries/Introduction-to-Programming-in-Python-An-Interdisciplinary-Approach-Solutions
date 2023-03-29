#sorted array constant ascending
#search value

a = [1,2,3,4,5,6,8,9,10,11]

def nonrecursivebinary(a,x):
    l = 0
    r = len(a)
    while l < r:
        mid = (l + r) // 2
        if a[mid] > x:
            r = mid
        elif a[mid] < x:
            l = mid + 1
        elif a[mid] == x:
            return mid
    return "x not in array"


print(nonrecursivebinary(a,5))