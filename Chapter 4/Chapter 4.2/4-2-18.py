#integer sort

a = [98 ,2, 3 ,1, 0, 0, 0, 3, 98 ,98, 2, 2 ,2 ,100 ,0 ,0 ,2]


def filterr(a):
    a.sort()
    l = 0
    while a[l] < 0:
        l += 1
    r = len(a)-1
    while a[r] > 99:
        r -= 1
    a = a[l:r]
    return a

a = filterr(a)

print(a)