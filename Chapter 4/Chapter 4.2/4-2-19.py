#floor and ceiling

a = [98 ,2, 3 ,1, 6, 0, 4, 3, 98 ,98, 2, 2 ,2 ,100 ,0 ,0 ,2]
a.sort()

#given a sorted array, compose floor and ceiling that give smallest / bigget index that is not smaller / bigger than the floor ceiling x.


def floor(a,x):
    if x > a[len(a)-1]: return a[len(a)-1]
    if x < a[0]: return "no floor found"

    l = 0
    r = len(a)

    while a[l] < x:
        mid = (l + r) // 2
        if a[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return a[l-1]

print(a)
print(floor(a,5))

def ceiling(a,x):
    if x > a[len(a)-1]: return "no ceiling found"
    if x < a[0]: return a[0]
    l = 0
    r = len(a)

    while a[l] < x:
        mid = (l + r) // 2
        if a[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return a[l]

print(a)
print(ceiling(a,0))