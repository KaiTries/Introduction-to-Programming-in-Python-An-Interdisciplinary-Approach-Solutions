import stdstats
from instream import InStream
import stddraw
import stdio

PRICE = InStream('9.close.txt')
VOLUME = InStream('9.volume.txt')


#store volume and price in readable array

prices = []
while PRICE.hasNextLine():
    x = PRICE.readLine()
    x = float(x)
    prices += [x]

prices = prices[1:]
prices = prices[::-1]
volumes = []
while VOLUME.hasNextLine():
    x = VOLUME.readLine()
    x = int(x)
    volumes += [x]

volumes = volumes[1:]
volumes = volumes[::-1]
#---------------------------

#given rate at which to plot(1 is daily, 7 is weekly etc.)
n = 1

#bars can disappear if the width is too small
if n <= 5:
    w = 10
elif n < 10:
    w = 0.75
else:
    w = 0.5

#start and end date (start date is: 1-Oct-1928 end date is: 17-Mar-06)
#max possible length is 28 292 days
start = 0
stop = 1000

if stop - start > 28292: 
    stdio.write("day range too big")
else:
    countprice = prices[start:stop:n]
    #if we plot them like this the prices will just be a red line at the bottom
    #we didive the volumes by 30000 to get a better visual representation 
    countvolume = volumes[start:stop:n]
    for i in range(len(countvolume)):
        countvolume[i] = int(countvolume[i])//100000

    stddraw.setXscale(0,len(countvolume))
    stddraw.setYscale(0,max(countprice))
    stdstats.plotBars(countvolume,w)
    stddraw.setPenColor(stddraw.RED)
    stdstats.plotLines(countprice)
    stddraw.show()

