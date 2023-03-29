#closest pair

#we again sort the array

#linearthmic time
a = [0,9,7,5,6,4,3,2,8]

def closestPair(a):
    a.sort()
    diff = 10
    pair = 0
    for i in range(len(a)-1):
        if a[i] == a[i+1]: return a[i],a[i+1]
        elif a[i+1] - a[i] < diff:
            diff = a[i+1] - a[i]
            pair = a[i+1],a[i]
    return pair


print(closestPair(a))