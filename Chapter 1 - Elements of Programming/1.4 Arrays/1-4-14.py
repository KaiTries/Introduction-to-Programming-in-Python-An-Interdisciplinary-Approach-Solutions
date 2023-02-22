import stdarray
import stdio

n = int(input("Enter size of matrix: "))

a = stdarray.create2D(n,n,1)



for i in range(1,n+1):
    for j in range(1,n+1):
        mn = min(i,j)
        for k in range(1,mn+1):
            if i%k == 0 and j%k == 0:
                hcf = k
            if hcf == 1:
                a[i-1][j-1] = True
            else:
                a[i-1][j-1] = False
            

for i in range(n+1):
    if i == 0:
        stdio.write("  ")
    else:
        stdio.write(str(i) + " ")
    for j in range(n):
        if i == 0:
            stdio.write(str(j+1) + " ")
        else:
            if a[i-1][j] == True:
                stdio.write("* ")
            else:
                stdio.write("  ")
    stdio.writeln()

