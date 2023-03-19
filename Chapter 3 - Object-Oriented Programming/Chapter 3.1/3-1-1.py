from charge import Charge
import sys
import stdio
w = 1

x0 = 0.5
y0 = 0.5

north = x0 , y0 + w
east = x0 + w, y0
south = x0, y0 - w
west = x0 - w, y0

x = 0.25
y = 0.5

cN = Charge(x0    ,y0 + w,1)
cE = Charge(x0 + w,y0    ,1)
cS = Charge(x0    ,y0 - w,1)
cW = Charge(x0 - w,y0    ,1)


vN = cN.potentialAt(x,y)
vE = cE.potentialAt(x,y)
vS = cS.potentialAt(x,y)
vW = cW.potentialAt(x,y)

stdio.writef('potential at (%.2f, %.2f) due to \n', x, y)
stdio.writeln(' ' + str(cN) + ' and')
stdio.writeln(' ' + str(cE) + ' and')
stdio.writeln(' ' + str(cS) + ' and')
stdio.writeln(' ' + str(cW))
stdio.writef('is %.2e\n', vN + vE + vS + vW)