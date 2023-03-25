#complex client
#solve ax**2 + bx + c = 0
from complex import Complex
import math




def solveComplexRoot(a,b,c):
    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant))/ (2*a)
        root2 = (-b - math.sqrt(discriminant))/ (2*a)
        return 'The roots are not complex and: ' + str(root1) + ', ' + str(root2)

    if discriminant == 0:
        root1 = -b / (2*a)
        return 'The root is not complex and only one exists: ' + str(root1)
    
    if discriminant < 0:
        real = (-b / (2*a))
        imaginary = (math.sqrt(abs(discriminant))/(2*a))
        return 'The roots are complex and are: ' + str(real) + ' + ' + str(imaginary)[:4] + 'i and ' + str(real) + ' - ' + str(imaginary)[:4] + 'i.'
    

print(solveComplexRoot(1,1,1))