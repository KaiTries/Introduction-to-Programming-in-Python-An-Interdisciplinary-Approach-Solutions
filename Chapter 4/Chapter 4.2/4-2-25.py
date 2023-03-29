#three sum


#find if the sum of two other array elements are exactly the opposite of current element
#again we sort first
#modify twosum to have an additional parameter to find x <- which we will use in our threeSum function
def twoSum(a,x,l,r):
    if a[0] > x or a[len(a)-1] < x or l == r: return -1
    if a[l] + a[r] == x: return a[l],a[r]
    if a[l] + a[r] > x: return twoSum(a,x,l,r-1)
    else: return twoSum(a,x,l+1,r)

a = [0,2,3,5,6,4,4,3,2,1]

def threeSum(a):
    a.sort()
    for i in range(len(a)):
        if twoSum(a[:i]+a[i+1:],-i,0,len(a)-2) != -1:
            return i, twoSum(a[:i]+a[i+1:],-i,0,len(a)-2)
    return "no threeSum"


print(threeSum(a))