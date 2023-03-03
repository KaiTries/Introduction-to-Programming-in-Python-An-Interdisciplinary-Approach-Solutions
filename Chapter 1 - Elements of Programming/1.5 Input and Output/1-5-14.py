import stdio
import sys

y = int(sys.argv[1])
m = 12*y                 #months
p = int(sys.argv[2])
r = float(sys.argv[3])
mr = (r/12)           #monthly interest rate




#stdio.writef(formats, month[i], pay, balance, interest)

monthly_payments = (p*(1+r*y))/m
interest = p*mr
interest_paid=interest
month = ['Jan','Feb','Mar','Apr','Mai','Jun','Jul','Aug','Sep','Oct','Nov','Dez']
stdio.writeln("Repayment of " + str(p) + " at the interest rate of " + str(r))
for i in range(y):
    stdio.writeln("--------------------")
    for j in range(len(month)):
        p = p - (monthly_payments - interest)
        stdio.writef('Year:%-2s %-4s %.2f %10.2f %10.2f \n',(i+1),month[j],monthly_payments,p,interest_paid)
        interest_paid += interest
    stdio.writeln("--------------------")