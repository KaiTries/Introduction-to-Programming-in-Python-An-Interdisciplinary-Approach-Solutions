#stock prices
#entry class
#table class
#input csv file


#Date,Open,High,Low,Close,Volume,Adj. Close*


from instream import InStream
import stdio


class Entry:


    def __init__(self, date, open, high, low, close, volume, adj_close):
            self._dte = date
            self._opn = open
            self._hih = high
            self._low = low
            self._clo = close
            self._vol = volume
            self._adj = adj_close
    
    def date(self):
         return str(self._dte)

    def price(self):
         return float(self._clo)
    
    def volume(self):
         return float(self._vol)

    def __str__(self) -> str:
          return str(self._dte) + ', ' + str(self._clo) + ', ' + str(self._vol)
    



class Table:
      

    def __init__(self, Input: str):
          self._input = InStream(Input)
          self._data = []
          while self._input.hasNextLine():
                x = self._input.readLine()
                x = x.split(',')
                x = Entry(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
                self._data += [x]

    def __len__(self):
        return len(self._data)

    def __getitem__(self,i: int) -> Entry:
        return self._data[i]

    def __str__(self):
        """
        print first 10 entries
        """
        [print(i) for i in self._data[:10]]
        return ''
    
    def avgBetweenDates(self,start: str,stop: str):
        """
        dates must be in format: '12-Jan-97' -> singular digit days written without the leading zero
        """
        start_index = 0
        end_index = 0

        for i in range(len(self)):
            if self[i].date() == start:
                start_index = i
                break
            if self[i].date() == stop:
                end_index = i 

        if start == stop:
            end_index = start_index
            days = 1
        else:
            days = (start_index - end_index )+1

        avgPrice = 0
        avgVolum = 0

        for i in range(start_index,end_index-1,-1):

             avgPrice += self[i].price()
             avgVolum += self[i].volume()
 
        stdio.writef('the average price in the timeframe is: %6.2f and the average volume is: %5.1f ',avgPrice/days,avgVolum/days)
         




table = Table('djia.csv')
print(table)

table.avgBetweenDates('10-Mar-06','13-Mar-06')