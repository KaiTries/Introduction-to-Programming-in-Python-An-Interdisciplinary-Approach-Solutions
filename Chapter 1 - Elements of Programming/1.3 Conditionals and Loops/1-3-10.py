#Compose a program that writes a table of the values of log n, n, n log n, n2, and n3 for n = 2, 4, 8, 16, 32, 64, 128. Use tabs ('\t' characters) to line up columns.

#-----------------------------------------------------------------------
# functiongrowth.py
#-----------------------------------------------------------------------

import stdio
import math

# Write to standard output ln N, N, N log N, N^2, N^3 for N = 2,
# 4, 8, ..., 2048.

MIN_N = 2
MAX_N = 2048

stdio.writeln('log N \tN \tN log N\tN^2 \tN^3')

i = MIN_N
while i <= MAX_N:
    stdio.write(int(math.log(i)))
    stdio.write('\t')
    stdio.write(i)
    stdio.write('\t')
    stdio.write(int(i * math.log(i)))
    stdio.write('\t');
    stdio.write(i * i)
    stdio.write('\t')
    stdio.write(i * i * i)
    stdio.writeln()
    i *= 2
    
#-----------------------------------------------------------------------

# python functiongrowth.py 
# log N   N       N log N N^2 	  N^3
# 0       2       1       4       8
# 1       4       5       16      64
# 2       8       16      64      512
# 2       16      44      256     4096
# 3       32      110     1024    32768
# 4       64      266     4096    262144
# 4       128     621     16384   2097152
# 5       256     1419    65536   16777216
# 6       512     3194    262144  134217728
# 6       1024    7097    1048576 1073741824
# 7       2048    15615   4194304 8589934592


#Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
#Last updated: Fri Oct 20 20:45:16 EDT 2017.