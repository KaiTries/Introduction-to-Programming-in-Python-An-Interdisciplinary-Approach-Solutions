#data analysis
import stdstats
import stddraw
import gaussianinv

class Data:
    """
    Data to handle arrays of tests -> run same test with different int control numbers
    -> compare each testresults against eachother
    -> example run percolation probability with different grid sizes 
    -> store the results for each grid size in this Data class
    -> use the plotTukey or plot function to illustrate the results
    """

    def __init__(self,n) -> list:
        self._data = n * [[]]


    def __len__(self):
        return len(self._data)
    
    def addDataPoint(self,i: int,x: float):
        if len(self._data[i]) < 1:
            self._data[i] = [x]
        else:
            self._data[i] += [x]

    def plot(self):
        for i in range(len(self)):
            stdstats.plotLines(self._data[i])


    def plotTukey(self):
        for i in range(len(self)):
            if len(self._data[i]) > 1:
                low = min(self._data[i])
                hih = max(self._data[i])
                x = stdstats.mean(self._data[i])
                stdv1 = stdstats.stddev(self._data[i])
                stddraw.line(i,low,i,hih)
                stddraw.filledRectangle(i-0.25,x-stdv1,0.5,2*stdv1)
                print(i)

    def __str__(self) -> str:
        return str(self._data)
    

