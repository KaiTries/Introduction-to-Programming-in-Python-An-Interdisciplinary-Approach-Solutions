#data type for uivariate polynomials
import random



class Polynomial:
    """
    accepts a tuple to create a polynomial data type (1,2,3) -> x^2 + x + 3
    length of tuple determines the degree so put 0s inbetween to leave some x^n out
    """

    def __init__(self,tuples: tuple):
        self._poly = tuples
        self._nums = list(tuples[:])
        self._degree = len(self._nums)-1

    def __str__(self):
        n = len(self._nums)
        for i in range(len(self._nums)):
            print(self._nums[i], end = "")
            if (i != n - 1):
                print("x^", n-i-1, end = "")
            if (i != n - 1):
                print(" + ", end = "")
        return ''


    def __add__(self, other):
        temp_self = list(self._nums)
        temp_other = list(other._nums)
        if len(temp_self) < len(temp_other):
            while len(temp_self) < len(temp_other):
                temp_self = [0] + temp_self
        if len(temp_self) > len(temp_other):
            while len(temp_self) > len(temp_other):
                temp_other = [0] + temp_other
        new_poly = []
        for i in range(len(temp_self)):
            new_poly += [temp_self[i] + temp_other[i]]
        return Polynomial(tuple(new_poly))
    
    def __sub__(self,other):
        temp_self = list(self._nums)
        temp_other = list(other._nums)
        if len(temp_self) < len(temp_other):
            while len(temp_self) < len(temp_other):
                temp_self = [0] + temp_self
        if len(temp_self) > len(temp_other):
            while len(temp_self) > len(temp_other):
                temp_other = [0] + temp_other
        new_poly = []
        for i in range(len(temp_self)):
            new_poly += [temp_self[i] - temp_other[i]]
        return Polynomial(tuple(new_poly))
    
    def __mul__(self,other):
        temp_self = self._nums
        temp_other = other._nums
        result = [0]*(len(temp_self)+len(temp_other)-1)
        for i in range(len(temp_self)):
            for j in range(len(temp_other)):
                result[i+j] = result[i+j] + temp_self[i] * temp_other[j]
        return Polynomial(tuple(result))
    
    def degree(self):
        return self._degree
    
    def eval(self,x):
        total = 0
        n = len(self._nums)
        for i in range(n):
            if self._nums[i] == 'C':
                i = i
            else:
                total += self._nums[i]*x**(n-1-i)
        if 'C' in self._nums: return str(total) + ' + C'
        else: return total
    
    def composition(self,other):
        new_poly = []
        for i in range(len(self._nums)):
            new_poly += [[self._nums[i]]+[tuple(other._nums)]]
        return Polynomial(tuple(new_poly))
    
    def differentiate(self):
        temp_array = self._nums
        n = len(temp_array)
        for i in range(n-1):
            temp_array[i] = temp_array[i]*(self._degree-i)
        temp_array = temp_array[:-1]
        return Polynomial(tuple(temp_array))
    
    def integrate(self):
        temp_array = self._nums
        n = len(temp_array)
        temp_array += ['C']
        n = len(temp_array)
        for i in range(n-2):
            temp_array[i] = temp_array[i]/(n-i-1)
        return Polynomial(tuple(temp_array))
    
    def __eq__(self, other):
        for i in range(10):
            x = random.randint(-100,100)
            if self.eval(x) != other.eval(x): return False
        return True


