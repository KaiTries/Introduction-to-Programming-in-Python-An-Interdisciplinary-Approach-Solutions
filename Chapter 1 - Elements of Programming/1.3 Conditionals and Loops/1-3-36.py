#median of 5


#input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
e = int(input("Enter the fifth number: "))

#compute the median of the 5 numbers

if a > b:
    if a > c:
        if a > d:
            if a > e:
                if b > c:
                    if b > d:
                        if b > e:
                            if c > d:
                                if c > e:
                                    if d > e:
                                        median = d
                                    else:
                                        median = e
                                else:
                                    median = c
                            else:
                                median = d
                        else:
                            median = e
                    else:
                        median = d
                else:
                    median = c
            else:
                median = b
        else:
            median = a
    else:
        median = c
else:
    if b > c:
        if b > d:
            if b > e:
                if a > c:
                    if a > d:
                        if a > e:
                            if c > d:
                                if c > e:
                                    if d > e:
                                        median = d
                                    else:
                                        median = e
                                else:
                                    median = c
                            else:
                                median = d
                        else:
                            median = e
                    else:
                        median = d
                else:
                    median = c
            else:
                median = b
        else:
            median = a
    else:
        median = c

#output
print("The median is: ", median)

print((a + b + c + d + e)/5)

