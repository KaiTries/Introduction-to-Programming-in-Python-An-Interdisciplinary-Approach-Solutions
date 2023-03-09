#calender 
import stdio
import sys

#------ Global Variables
months = ["January","February","March","April","Mai","June","July","August","September","October","November","Dezember"]
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]


#------ Functions


#------ Leapyear
def _isleap(y):
    isLeapYear = (y % 4 == 0)
    isLeapYear = isLeapYear and (y % 100 != 0)
    isLeapYear = isLeapYear or  (y % 400 == 0)
    return isLeapYear


#------ day 0-6
def _day(m,d,y):
    y0 = y - (14 - m) // 12
    x = y0 + y0//4 - y0//100 + y0//400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31*m0)//12) % 7
    return d0



#------ Length of Month
def _month(m,y):
    a = []
    if m == 2:
        if _isleap(y):
            days = 29
            for i in range(days):
                x = _day(m,i,y)
                a += [x]
            return a
        else:
            days = 28
            for i in range(days):
                x = _day(m,i,y)
                a += [x]
            return a            
    elif m%2 == 0 and m != 8:
        days = 30
        for i in range(days):
            x = _day(m,i,y)
            a += [x]
        return a
    else:
        days = 31
        for i in range(days):
            x = _day(m,i,y)
            a += [x]
        return a        


#------ Input
m = int(sys.argv[1])
y = int(sys.argv[2])

#------ Processing

x = _month(m,y)



#------ Output
stdio.writef('%12.10s %4s \n',months[m-1],y)
for i in range(7):
    stdio.writef('%-4.3s',days[x[i]])
stdio.writeln()
for i in range(len(x)):
    if (i+1)%7 == 0 and i != 0:
        stdio.writef('%3.3s \n',i+1)
    else:
        stdio.writef('%3.3s ',i+1)


#couldnt figure out how to adapt the numbers to the days so i adapted starting day to number 1