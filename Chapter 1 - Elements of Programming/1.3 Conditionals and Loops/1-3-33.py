#compute CHECKSUM digit

import math

#input

n = int(input("Enter the number(9 digit integer): "))

#compute CHECKSUM digit

n1 = n // 100000000
print("n1: ", n1)
n2 = (n // 10000000) % 10
print("n2: ", n2)
n3 = (n // 1000000) % 10
print("n3: ", n3)
n4 = (n // 100000) % 10
print("n4: ", n4)
n5 = (n // 10000) % 10
print("n5: ", n5)
n6 = (n // 1000) % 10
print("n6: ", n6)
n7 = (n // 100) % 10
print("n7: ", n7)
n8 = (n // 10) % 10
print("n8: ", n8)
n9 = n % 10
print("n9: ", n9)

for x in range(10):
    checksum = (n1*10 + n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2 + x) % 11
    if checksum == 0:
        print("CHECKSUM digit: ", x)
        break

