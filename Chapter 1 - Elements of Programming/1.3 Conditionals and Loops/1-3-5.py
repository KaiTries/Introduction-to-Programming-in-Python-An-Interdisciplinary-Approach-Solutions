#What is the value of j after each of the following code fragments is executed?
#
#a. j = 0
#   for i in range(0, 10):
#       j += i
#   
#   
#
#b. j = 1
#   for i in range(0, 10):
#       j += j
#
#c. for j in range(0, 10):
#       j += j
#
j = 0
for i in range(0, 10):
       j += i

print (j)

j = 0
for i in range(0, 10):
       j += j

print (j)

for j in range(0, 10):
       j += j

print (j)


#What is the value of j after each of the following code fragments is executed?
#
#45
#0
#18