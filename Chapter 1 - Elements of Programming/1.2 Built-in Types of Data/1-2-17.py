#Compose a program that writes the sum of two random integers between 1 and 6 (such as you might get when rolling dice).

import random
import stdio

stdio.writeln(random.randint(1,6) + random.randint(1,6))
#random.randint includes the upper bound in the range of possible values.

#you can also assign the random integers to variables and then add them together.
#This is more readable and easier to debug.

# import random
# import stdio
#
# a = random.randint(1,6)
# b = random.randint(1,6)
# stdio.writeln(a + b)

