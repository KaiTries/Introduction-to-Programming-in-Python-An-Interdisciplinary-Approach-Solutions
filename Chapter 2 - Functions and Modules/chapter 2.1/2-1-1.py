def max3(a,b,c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


a = 1 
b = 2.5
c = 2

print(max3(a,b,c))