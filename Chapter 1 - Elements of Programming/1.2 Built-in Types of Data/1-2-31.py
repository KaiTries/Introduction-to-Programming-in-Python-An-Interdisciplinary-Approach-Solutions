#Three-sort. Compose a program that accepts three integers from the command line and writes them in ascending order. Use the built-in min() and max() functions.

#-----------------------------------------------------------------------
# threesort.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept three integers from the command-line, and write them to
# standard output in ascending order.

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

# Compute stats.
minimum = min(a, b, c)
maximum = max(a, b, c)
median = a + b + c - minimum - maximum;

# Write stats.
stdio.writeln(minimum)
stdio.writeln(median)
stdio.writeln(maximum)

#-----------------------------------------------------------------------

# python threesort.py 18 25 74
# 18
# 25
# 74

# python threesort.py 74 18 25
# 18
# 25
# 74



#Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
#Last updated: Fri Oct 20 20:45:16 EDT 2017.