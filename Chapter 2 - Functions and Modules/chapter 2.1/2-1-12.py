import math
import sys
import stdio
import stdarray


#--------------------------FUNCTIONS
def fsum(n):                                        #function to sum up the decimal points that get multiplied
    number = n
    number_string = str(n)
    digits= []
    for i in range(len(number_string)):
        digits += [int(number_string[i])]
    return sum(digits)

def f(n):                                           #function to calculate the checksum with 1*d + 2*d pattern
    number = n
    number_string = str(n)
    digits= []
    for i in range(len(number_string)):
        digits += [int(number_string[i])]
    
    for i in range(len(digits)):
        if i%2!=0:
            digits[i] = fsum(2*digits[i])
        else:
            digits[i] = digits[i]


    return digits




#---------------------INPUT
n = int(sys.argv[1])



#--------------------GLOBAL CODE
x = f(n)
if sum(x)%10 != 0:
    stdio.writeln("not a valid checksum") 
else:
    for i in range(len(x)):
        stdio.write(x[i])
    stdio.write(sum(x)%10)

