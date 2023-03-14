import stdstats
import stddraw

def overlay(a,b,a1,b1):
    """
    Plots two arrays over each other. last two params are if you want lines or bars
    choose 1 or 2 respectively
    """
    if a1 == 1:
        stdstats.plotLines(a)
    if a1 == 2:
        stdstats.plotBars(a)
    stddraw.setPenColor(stddraw.BLUE)
    if b1 == 1:
        stdstats.plotLines(b)
    if b1 == 1:
        stdstats.plotBars(b)
