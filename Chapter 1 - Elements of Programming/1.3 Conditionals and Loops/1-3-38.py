import math

#calculate cosine of angle
x = float(input("Enter the angle in radians: "))
#convert

twoPi = 2 * math.pi
while x > twoPi:
    x -= twoPi  
while x < twoPi:
    x += twoPi


term = 1
total = 0

i = 1
while term != 0:
    term *= (x / i)
    if i % 4 == 1:
        total += term
    elif i % 4 == 3:
        total -= term
    i += 1



print("sine of angle: ", total)


#calculate cosine of angle
#convert

twoPi = 2 * math.pi
while x > twoPi:
    x -= twoPi  
while x < twoPi:
    x += twoPi


cos_approx = 0
n = 5

def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_approx += ( coef ) * ( (num)/(denom) )
    
    return cos_approx

print("cosine of angle: ", func_cos(x, n))