#count primes in a range n
#prime numbers are only divisible by 1 and themselves
import stdio
#input

n = int(input("Enter the number: "))

#compute
count = 0
for i in range (n):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            count += 1   

#output
print("Number of primes in range: ", count)
