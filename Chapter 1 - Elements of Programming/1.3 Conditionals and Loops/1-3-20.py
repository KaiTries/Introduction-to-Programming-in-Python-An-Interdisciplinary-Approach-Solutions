import math


n = int(input("first number:"))


s = ""
v = 1

while v <= n // 2:
    v *= 2

while v > 0:
    if n < v:
        s += "0"
    else:
        s += "1"
        n -= v
    v //= 2

print(s)


m = int(input("second number:"))
t = ""
r = 0

while m >0:
    t = str(m % 2) + t
    m = m // 2

print(t)