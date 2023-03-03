import stddraw

# Draw a bouncing ball to standard draw.

RADIUS = .05
DT = 20.0

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

rx = .480
ry = .860
vx = .015
vy = .023


stddraw.clear(stddraw.GRAY)
while True:
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.filledCircle(rx, ry, RADIUS)
    # Update ball position and draw it there.
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy
    rx = rx + vx
    ry = ry + vy


    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(DT)
    