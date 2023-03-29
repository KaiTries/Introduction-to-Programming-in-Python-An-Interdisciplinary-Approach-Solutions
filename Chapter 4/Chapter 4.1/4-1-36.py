#factorial algorithm
import sys



#basic one:
#will struggle after 100
N = 10
f = 1
for i in range(2,N+1):
    f *= i

#this one does the trick





def factorial(n):
    res = [None]*100000
    # Initialize result
    res[0] = 1
    res_size = 1
 
    # Apply simple factorial formula
    # n! = 1 * 2 * 3 * 4...*n
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x = x + 1
 
    return res
 
 
# This function multiplies x with the number
# represented by res[]. res_size is size of res[]
# or number of digits in the number represented
# by res[]. This function uses simple school
# mathematics for multiplication. This function
# may value of res_size and returns the new value
# of res_size
def multiply(x, res, res_size):
 
    carry = 0  # Initialize carry
 
    # One by one multiply n with individual
    # digits of res[]
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10  # Store last digit of
        # 'prod' in res[]
        # make sure floor division is used
        carry = prod//10  # Put rest in carry
        i = i + 1
 
    # Put carry in res and increase result size
    while (carry):
        res[res_size] = carry % 10
        # make sure floor division is used
        # to avoid floating value
        carry = carry // 10
        res_size = res_size + 1
 
    return res_size
 


 
#compute the longest run of 9's in 1000000! 

def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        rtn = range_prod(lo,mid) * range_prod(mid+1,hi)
    elif lo == hi:
        rtn = lo
    else: rtn = hi
    return reduce_10(rtn)

def reduce_10(n):
    while not n % 10:
        n //= 10
    return n


def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)

number = treefactorial(1000000)

count = 0
maxcount = 0
while number > 0:
    if number%10 == 9: 
        count += 1
        number = number // 10
    else:
        if count > maxcount:
            maxcount = count
        count = 0
        number = number // 10

print(maxcount)
