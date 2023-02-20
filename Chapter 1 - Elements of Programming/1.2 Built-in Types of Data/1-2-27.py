#Uniform random numbers. Compose a program that writes five uniform random floats between 0 and 1, their average value, and their minimum and maximum value. 
#Use the built-in max() and min() functions.

#-----------------------------------------------------------------------
# stats1.py
#-----------------------------------------------------------------------

import stdio
import random

# Generate 5 random floats between 0.0 and 1.0. Write them to
# standard output, along with their average value, the min value,
# and the max value.

N = 5

# Generate 5 random floats.
x1 = random.random()
x2 = random.random()
x3 = random.random()
x4 = random.random()
x5 = random.random()

# Write the 5 random floats.
stdio.writeln(x1)
stdio.writeln(x2)
stdio.writeln(x3)
stdio.writeln(x4)
stdio.writeln(x5)

# Compute the stats.
minimum = min(x1, x2, x3, x4, x5)
maximum = max(x1, x2, x3, x4, x5)
average = (x1 + x2 + x3 + x4 + x5) / N

# Write the stats.
stdio.writeln('Average = ' + str(average))
stdio.writeln('Min     = ' + str(minimum))
stdio.writeln('Max     = ' + str(maximum))

#-----------------------------------------------------------------------

# python stats1.py      
# 0.556496926354658
# 0.513350209165622
# 0.2388414489512366
# 0.6624155966015689
# 0.9627794290136971
# Average = 0.5867767220173565
# Min     = 0.2388414489512366
# Max     = 0.9627794290136971

# python stats1.py
# 0.6478938018093143
# 0.4962425246577342
# 0.4813720971364449
# 0.3713682192048282
# 0.22171061570089612
# Average = 0.44371745170184357
# Min     = 0.22171061570089612
# Max     = 0.6478938018093143



#Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
#Last updated: Fri Oct 20 20:45:16 EDT 2017.