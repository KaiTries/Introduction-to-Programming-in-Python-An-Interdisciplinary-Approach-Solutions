#majority

#if an element occurs more than n/2 times n is length of array
#False
a = [0,2,3,5,6,4,4,3,2,1]
#True
b = [0,2,4,4,4,4,4,4,2,1]


#one approach is to go through the array and counting and reseting
#if end count > n/2 we have majority
def majority(a):
    a.sort()
    current_count = 1
    max_count = 0
    majority = 0
    for i in range(1,len(a)):
        if a[i] > a[i-1]:
            if current_count > max_count:
                max_count = current_count
                majority = a[i]
            current_count = 1
        else: current_count += 1
    if current_count > (len(a)/2): return majority
    return False




#is doable with hashes but theyre not in the book so idk
#this is also linear so the better solution
def Majority(a):
    storage = {}
    n = len(a)
    for i in range(n):
        if a[i] in storage:
            storage[a[i]] += 1
        else:
            storage[a[i]] = 1


    hasMajority = False
    
    for value in storage:
        if storage[value] > n / 2: 
            hasMajority = True
            return hasMajority
    return hasMajority

Majority(b)