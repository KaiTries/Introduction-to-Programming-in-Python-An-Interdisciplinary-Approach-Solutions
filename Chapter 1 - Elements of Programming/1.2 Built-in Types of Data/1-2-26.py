#Day of the week. Compose a program that accepts a date as input and writes the day of the week on which that date falls. 
#Your program should accept three command-line arguments: m (month), d (day), and y (year). For m use 1 for January, 2 for February, and so forth. 
#For output write 0 for Sunday, 1 for Monday, 2 for Tuesday, and so forth. Use the following formulas for the Gregorian calendar:
#y0 = y - (14 - m) / 12
#x = y0 + y0/4 - y0/100 + y0/400
#m0 = m + 12 * ((14 - m) / 12) - 2
#d0 = (d + x + (31*m0)/ 12) mod 7
#For example, on what day of the week was August 2, 1953?
#
#y = 1953 - 0 = 1953
#x = 1953 + 1953/4 - 1953/100 + 1953/400 = 2426
#m = 8 + 12*0 - 2 = 6
#d = (2 + 2426 + (31*6) / 12) mod 7 = 2443 mod 7 = 0 (Sunday)
#

#-----------------------------------------------------------------------
# day.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integers representing a month (m), day (d), and year (y) as
# command-line arguments. Write to standard output the day of the week
# of the date m/d/y according to the Gregorian calendar. For m use 1
# for January, 2 for February, and so forth. For the day of the week
# use 0 for Sunday, 1 for Monday, and so forth.

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

y0 = y - (14 - m) // 12
x = y0 + y0//4 - y0//100 + y0//400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + (31*m0)//12) % 7

stdio.writeln(d0)

#-----------------------------------------------------------------------

# python day.py 8 2 1953
# 0



#Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
#Last updated: Fri Oct 20 20:45:16 EDT 2017.