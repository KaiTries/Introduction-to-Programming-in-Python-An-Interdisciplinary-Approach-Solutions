#Dragon curve. Compose a program to write the instructions for drawing the dragon curves of order 0 through 5. The instructions are strings of the characters F, L, and R, where F means "draw line while moving 1 unit forward", L means "turn left", and R means turn right. A dragon curve of order n is formed when you fold a strip of paper in half n times, then unfold to right angles. The key to solving this problem is to note that a curve of order n is a curve of order n-1 followed by an L followed by a curve of order n-1 traversed in reverse order, and then to figure out a similar description of the reverse curve.

#-----------------------------------------------------------------------
# dragon1.py
#-----------------------------------------------------------------------

import stdio

# Write to standard output the instructions for drawing a dragon curve
# of orders 0 through 5.

dragon0 = 'F'
nogard0 = 'F'
dragon1 = dragon0 + 'L' + nogard0
nogard1 = dragon0 + 'R' + nogard0
dragon2 = dragon1 + 'L' + nogard1
nogard2 = dragon1 + 'R' + nogard1
dragon3 = dragon2 + 'L' + nogard2
nogard3 = dragon2 + 'R' + nogard2
dragon4 = dragon3 + 'L' + nogard3
nogard4 = dragon3 + 'R' + nogard3
dragon5 = dragon4 + 'L' + nogard4

stdio.writeln(dragon0)
stdio.writeln(dragon1)
stdio.writeln(dragon2)
stdio.writeln(dragon3)
stdio.writeln(dragon4)
stdio.writeln(dragon5)

#-----------------------------------------------------------------------

# python dragon1.py     
# F
# FLF
# FLFLFRF
# FLFLFRFLFLFRFRF
# FLFLFRFLFLFRFRFLFLFLFRFRFLFRFRF
# FLFLFRFLFLFRFRFLFLFLFRFRFLFRFRFLFLFLFRFLFLFRFRFRFLFLFRFRFLFRFRF


#Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
#Last updated: Fri Oct 20 20:45:16 EDT 2017