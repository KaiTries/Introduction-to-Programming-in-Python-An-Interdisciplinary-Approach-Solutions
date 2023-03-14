import stdio
def ex233(n):
    if n <= 0: return 
    stdio.writeln(n)
    ex233(n-2)
    ex233(n-3)
    stdio.writeln(n)


ex233(6)

#output is: #6
            #4
            #2
            #2
            #1
            #1
            #4
            #3
            #1
            #1
            #3
            #6

#i recommend drawing the function tree and then reading it from left to right to get a sense of recursion