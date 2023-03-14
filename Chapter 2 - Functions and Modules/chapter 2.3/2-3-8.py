def mystery(a, b):
    if b == 0:
        return 0
    if b % 2 == 0:
        return mystery(a+a, b//2)
    return mystery(a+a, b//2) + a

print(mystery(2,25))
#50
print(mystery(3,11))
#33

#it computes a*b
#if we replace + with * and 0 with 1 it will compute a**b