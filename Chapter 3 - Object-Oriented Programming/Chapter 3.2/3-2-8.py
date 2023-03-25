#interval data type



class Interval:


    def __init__(self,left,right):
        if left > right:
            left = None
            right = None
        self._left = left
        self._right = right

    def intersects(self,other):
        if other._right == None or self._right == None:
            return False
        if self._right < other._left:
            return False
        if self.contains(other):
            if self._right == other._left or self._right == other._right:
                return True
            if self._left == other._left or self._right == other._right:
                return True
            return False
        return True
    
    def contains(self,other):
        if other._right == None or self._right == None:
            return False
        if self._right >= other._right and self._left <= other._left:
            return True
        return False
    
    def __str__(self):
        if self._right == None:
            return '[]'
        return '[' + str(self._left) + ', ' + str(self._right) + ']'
    

