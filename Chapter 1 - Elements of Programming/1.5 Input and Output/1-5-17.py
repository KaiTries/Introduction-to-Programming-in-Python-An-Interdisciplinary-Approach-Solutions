import stdio



a = []
while not stdio.isEmpty():
    x = stdio.readFloat()
    if x < 1 and x > -1: 
        a += [x]

avg_mag = 0
for i in range(len(a)):
    avg_mag += abs(a[i])

avg_mag = avg_mag / len(a)

avg_pwr = 0
for i in range(len(a)):
    avg_pwr += (a[i])**2

avg_pwr = avg_pwr / len(a)

crossings = 0
for i in range(len(a)-1):
    if (a[i] > 0 and a[i+1] < 0) or (a[i] < 0 and a[i+1] > 0):
        crossings += 1


stdio.writef('the average magnitude is %3.2f\nThe average power is %3.2f\nThe number of zero crossings is %1i',avg_mag,avg_pwr,crossings)