#two sum


a = [0,2,3,5,6,-4,4,3,2,1]
a.sort()
#start left and right move depending if higher or lower than zero
def twoSum(a,l,r):
    print(a)
    if a[0] > 0 or a[len(a)-1] < 0 or l == r: return False
    if a[l] + a[r] == 0: return True
    if a[l] + a[r] > 0: return twoSum(a,l,r-1)
    else: return twoSum(a,l+1,r)



print(twoSum(0,len(a)-1))