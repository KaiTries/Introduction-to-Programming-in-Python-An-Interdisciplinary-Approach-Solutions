#greatest common divisor

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

#we use euclid's algorithm to find the gcd

if x > y:
    if x % y == 0:
        print("the common divisor is", y)
    else:
        while x % y != 0:
            x, y = y, x % y
        print("the common divisor is", y)
elif y > x:
    if y % x == 0:
        print("the common divisor is", x)
    else:
        while y % x != 0:
            y, x = x, y % x
        print("the common divisor is", x)