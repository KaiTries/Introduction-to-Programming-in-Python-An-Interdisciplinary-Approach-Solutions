#nonrecursive percolation
import stdarray
import percolationio
import stdio

def draw(N):                                            #draw function so we can illustrate our result in command line
    yes = "*"
    no = " "
    for i in range(len(N)+1):
        if i == 0:
            stdio.writef('%-4s',no)
        else:
            stdio.writef('%-4s',str(i))
        for j in range(len(N)):
            if i == 0:
                stdio.writef('%-4s',str(j+1))
            else:
                if N[i-1][j] == True:
                    stdio.writef('%-4s',yes)
                else:
                    stdio.writef('%-4s',no)
        stdio.writeln()

def percolation(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n,n,False)
    for i in range(n):
        for j in range(n):
            if i == 0:                                  #first row is the same as Input, sets base
                isFull[i][j] = isOpen[i][j]
            elif isFull[i-1][j] and isOpen[i][j]:       #checks if the above square and the actual square are true
                isFull[i][j] = True                     #if both true we fill the square
                for k in range(j,-1,-1):                #we go backwards from that square filling each open square in that row until we hit a blocked square
                    if isOpen[i][k]:
                        isFull[i][k] = True
                    else:
                        break
                for k in range(j,n):                    #then we go forward in that row until we hit a blocked square
                    if isOpen[i][k]:
                        isFull[i][k] = True
                    else:
                        break                
    return isFull




#Global code to create a random 5x5 grid and test our new function

n = 5
array = percolationio.random(n,n,0.5)
draw(array)
draw(percolation(array))