#check validity ISBN number
#the new thing here is just to clean up a ISBN number
#meaning to remove a hyphen if they are inserted


#compute CHECKSUM digit

import math
from instream import InStream


#compute CHECKSUM digit this gives me the correct checksum
def CHECKSUM(n):
    n1 = n // 100000000
    n2 = (n // 10000000) % 10
    n3 = (n // 1000000) % 10
    n4 = (n // 100000) % 10
    n5 = (n // 10000) % 10
    n6 = (n // 1000) % 10
    n7 = (n // 100) % 10
    n8 = (n // 10) % 10
    n9 = n % 10
    for x in range(10):
        checksum = (n1*10 + n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2 + x) % 11
        if checksum == 0:
            return int(str(n) + str(x))

#input
#modifing the input to make it computable
#i added two lines of ISBN numbers in in1.text for testing
#these are the two lines:
#132-562-2340
#132-562-2346

INPUT = InStream('in1.txt')

#computation

while INPUT.hasNextLine():
    ISBN_Numbers = INPUT.readLine()
    ISBN_Numbers = ISBN_Numbers.replace('-','')
    ISBN_lessCHECK = ISBN_Numbers[:-1]
    if CHECKSUM(int(ISBN_lessCHECK)) == int(ISBN_Numbers):
        print(ISBN_Numbers,' is valid')
    else:
        print(ISBN_Numbers, ' is not valid')
