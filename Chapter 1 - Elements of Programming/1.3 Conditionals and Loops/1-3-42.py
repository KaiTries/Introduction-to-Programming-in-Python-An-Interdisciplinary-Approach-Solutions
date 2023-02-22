import math

x = 0.01
t = int(input("Enter a number between 0 and 100: "))
r = float(input("Enter a number between 0 and 4: "))


x = 1 / (1+((1/x) - 1)*math.e**(-r*t))


print(x)

