#Suppose that a and b are booleans. Show that the expression:
#(not (a and b) and (a or b)) or ((a and b) or not (a or b))
#evaluates to True.

a = True
b = True

print((not (a and b) and (a or b)) or ((a and b) or not (a or b)))

#Output:
#True

