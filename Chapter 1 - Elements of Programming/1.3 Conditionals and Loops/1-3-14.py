import math
import sys

#calculate continously compounded interest

#input
p = float(sys.argv[1]) #principal
r = float(sys.argv[2]) #interest rate
t = float(sys.argv[3]) #time

#process
a = p * math.e**(r*t)


#output

print ("The amount is", a)

#write a table giving the total amount paid and the remaining principal after each monthly payment.
