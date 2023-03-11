import stdio
import sys




#------global variables

mon = ["January","February","March","April","Mai","June","July","August","September","October","November","Dezember"]
day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

#------functions

#------check if leap year

def _leap(y):
    isLeapYear = (y % 4 == 0)
    isLeapYear = isLeapYear and (y % 100 != 0)
    isLeapYear = isLeapYear or  (y % 400 == 0)
    return isLeapYear

#------day assigmnet -> falls on which weekday

def _day(y,m,d):
    y0 = y - (14 - m) // 12
    x = y0 + y0//4 - y0//100 + y0//400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31*m0)//12) % 7
    return d0

#------define length of month and fill with weekdays

def _month(y,m):
    if m == 2:
        if _leap(y):
            days = 29
            a = []
            for i in range(1,days+1):
                a += [_day(y,m,i)]
            return a
        else:
            days = 28
            a = []
            for i in range(1,days+1):
                a += [_day(y,m,i)]           
            return a
    elif m%2 != 0 or m == 8:
        days = 31
        a = []
        for i in range(1,days+1):
            a += [_day(y,m,i)]           
        return a       
    else:
        days = 30
        a = []
        for i in range(1,days+1):
            a += [_day(y,m,i)]           
        return a          

#------add filler so that calender is aligned

def _fixedSun(a):
    if a[0] == 0:
        return a
    else:
        diff = a[0]
        x = []
        for i in range(diff):
            x += [0]
        x += a
        return x

#------Full function

def calender(y,m):
    a = _month(y,m)
    x = _fixedSun(a)
    diff = (len(x)-len(a))-1
    empty = " "
    stdio.writef('%12.10s %4.4s \n', mon[m-1],y)
    for i in range(len(day)):
        stdio.writef('%3.2s',day[i])
    stdio.writeln()  
    for i in range(len(x)):
        if i <= diff:
            stdio.writef('%3.2s',empty)
        elif (i+1)%7 == 0:
            stdio.writef('%3.2s \n',i-diff)        
        else:
            stdio.writef('%3.2s',i-diff)
    return stdio.writeln()

#------global code 

stdio.write("Please enter year: ")
y = stdio.readInt()
stdio.write("Please enter month: ")
m = stdio.readInt()
stdio.writeln()

calender(y,m)