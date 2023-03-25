#statistics
import math


class DataSetN:



    def __init__(self):
        self._num = 0
        self._sum = 0
        self._sumSQ = 0

    def addDataPoint(self,i):
        """
        add a datapoint to the set
        """
        self._num += 1
        self._sum += i
        self._sumSQ += i**2

    def datapoints(self):
        """
        returns number of data points
        """
        return self._num
    
    def mean(self):
        """
        returns the mean of the dataset
        """
        return self._sum / self._num
    
    def stdv(self):
        """
        returns the standard deviation of the dataset
        """
        return math.sqrt((self._sumSQ -self._sum**2/self._num)/(self._num - 1))
    
    def var(self):
        """
        variance of dataset
        """
        return self.stdv()**2
    



class datasetA:



    def __init__(self):
        self._data = []


    def addDataPoint(self,i):
        """
        add a datapoint to the set
        """
        self._data += [i]

    def datapoints(self):
        """
        returns number of data points
        """
        return len(self._data)
    
    def sum(self):
        sum = 0
        for i in range(len(self._data)):
            sum += self._data[i]
        return sum
    
    def mean(self):
        """
        returns the mean of the dataset
        """
        return self.sum() / self.datapoints()
    
    def stdv(self):
        """
        returns the standard deviation of the dataset
        """
        sum = 0
        for i in range(len(self._data)):
            sum += (self._data[i] - self.mean())**2
        
        return math.sqrt(sum/(self.datapoints()-1))
    
    def var(self):
        """
        variance of dataset
        """
        return self.stdv()**2
    
    