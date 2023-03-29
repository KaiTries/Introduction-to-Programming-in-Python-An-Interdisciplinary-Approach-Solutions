#common element
#three arrays find the elements that are in all three of them

#again sorting always a good move
#we can exlude arrays whos starting index are higher then the others end index
#actual algorithm is divide and conquer
#start with the first two arrays and find the common intersection
#then test that intersection against the third array

def intersect(a,b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    resultarray = []
    while i < (len(a))and j < (len(b)):
        if a[i] == b[j]:
            resultarray +=[a[i]]
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    return resultarray

def commonThree(a,c,b):
    firstIntersect = intersect(a,b)
    second_intersect = intersect(firstIntersect,c)
    return second_intersect

a = [4,3,2,1]
b = [0,2,3,5,]
c = [3,6]

print(commonThree(a,b,c))