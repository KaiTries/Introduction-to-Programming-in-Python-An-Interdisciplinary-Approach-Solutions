#game of life
#rules:
#including diagonals!!
#dead cell with exactly 3 live neighbours becomes live
#live cell with exactly 1 live neighbour becomes dead
#a live cell with more than three live neighbors becomes dead
#we will supplement a start matrix

#logic:
#if the sum of surrounding cells is 3 -> then a dead cell becomes alive
#if the sum of surrounding cells is 1 -> alive cell becomes dead
#if the sum of surrounding cells is >3 -> alive cell becomes dead

import percolationio
import stddraw
import stdarray

def matrix(n,p):                               
    return percolationio.random(n,n,p)                

def total(n,i,j):                               
    x = len(n)                                  
    top_mid     = n[(i-1)%x][j]
    top_left    = n[(i-1)%x][(j-1)%x]
    top_right   = n[(i-1)%x][(j+1)%x]
    left        = n[i][(j-1)%x]
    right       = n[i][(j+1)%x]
    bot_mid     = n[(i+1)%x][j]
    bot_left    = n[(i+1)%x][(j-1)%x]
    bot_right   = n[(i+1)%x][(j+1)%x]
    return int(top_mid+top_left+top_right+left+right+bot_mid+bot_left+bot_right)    

def game(start,t):
    stddraw.clear()                           
    percolationio.draw(start,True)
    stddraw.show(1000)
    if t == 0:                                
        return
    length = len(start)
    end = []
    end = stdarray.create2D(length,length,False)
    for i in range(length):
        for j in range(length):
            end[i][j] = start[i][j]
            #get the total of surrounding blocks:
            sums = total(start,i,j)
            if start[i][j]:
                if (sums < 2) or (sums > 3):
                    end[i][j] = False
            else:
                if sums == 3:
                    end[i][j] = True  
    game(end,t-1)

n = matrix(100,0.2)
n[2][3] = True
n[3][4] = True
n[4][2] = True
n[4][3] = True
n[4][4] = True

print(total(n,3,2))

game(n,100)

stddraw.show()





