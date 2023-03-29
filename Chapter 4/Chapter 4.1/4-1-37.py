#linear time algo that find a contigous subsequence of at most m in a sequence of n with highest sum


nums1 = [-2,1,-3,4,-1,2,1,-5,4]

maximum = nums1[0]
current = 0
for i in range(len(nums1)):
    current += nums1[i]
    if(current>maximum):
        maximum = current
    if current < 0:
        current = 0

print(maximum)
