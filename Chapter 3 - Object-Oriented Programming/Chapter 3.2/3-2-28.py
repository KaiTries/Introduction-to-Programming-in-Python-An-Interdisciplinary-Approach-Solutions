#Elements
from instream import InStream

class Element:

    """
    Stores elements in an appropriate Data-type
    """

    def __init__(self,Element,Number,Symbol,Weight):
        self._ele = Element
        self._num = Number
        self._sym = Symbol
        self._wei = Weight

    def name(self: str) -> str:
        return str(self._ele)

    def number(self: int) -> int:
        return int(self._num)

    def symbol(self: str) ->  str:
        return str(self._sym)

    def weight(self: float) -> float:
        return float(self._wei)


    

    def __str__(self) -> str:
        return str(self._ele) + ', ' + str(self._num) + ', ' + str(self._sym) + ', ' + str(self._wei)
    


water = Element('Hydrogen',1,'H',1.01)

print(water.weight())


class PeriodicTable:


    def __init__(self):
        self._data = []

    def read(self,input):
        input = InStream(input)
        while input.hasNextLine():
            x = input.readLine()
            x = x.split(',')
            element = Element(x[0],x[1],x[2],x[3])
            self._data += [element]

    def __len__(self):
        return len(self._data)

    def __str__(self):
        [print(i) for i in self._data]
        return ''

    def givenSymbol(self, symbol: str) -> int:
        """
        Input the Symbol get the Number -> H -> 1
        """
        for i in range(len(self)):
            if self._data[i].symbol() == symbol:
                return i

    def MolecWeight(self, combination: str) -> float:
        x = combination
        x = list(x)
        for i in range(len(x)-2):
            if x[i+1].islower():
                x[i] = x[i] + x[i+1]
                x.pop(i+1)
        
        weight = 0
        print(x)
        for i in range(len(x)):
            if x[i].isdigit():
                i = i
            else:
                e = table.givenSymbol(x[i])
                element = self._data[e]
                print(element)
                if i < len(x)-2:
                    if x[i+1].isdigit():
                        weight += int(x[i+1]) * element.weight()
                    else:
                        weight += element.weight()
                else:
                    weight += element.weight()
        return weight


table = PeriodicTable()

table.read('elements.csv')

print(table.MolecWeight('H2O'))