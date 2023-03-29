



#given array liniar time


a = [1,2,3,4,5]


for i in range(len(a)):
    if i+1 != a[i]:
        print (i+1)

b = (1,2,3,4,5,5)
#given a read only array do and every value occurs once and one twice
for i in range(len(b)):
    if i+1 != b[i]:
        print (b[i])

#given a read only array with values between 1 and n-1, one occurs twice 
#values do not correspond to len anymore

c = (3,5,1,2,4,1)
result=[]
for i in range(len(c)):
    if c[i] in c[i+1:]:
        print(c[i])
