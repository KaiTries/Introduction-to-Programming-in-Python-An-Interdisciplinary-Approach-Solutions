#time
import time



class dayTime:


    def __init__(self):
        self._time = int(time.time()%86400)

    def __str__(self) -> str:
        return str(self.hour()) + ':' + str(self.minute()) + ':' + str(self.second())
    
    def hour(self):
        _a = self._time//3600
        return _a
    
    def minute(self):
        _a = self._time%3600//60
        return _a
    
    def second(self):
        _a = self._time%60
        return _a


class dayTime3:


    def __init__(self):
        self._seconds = int(time.time()%86400)%60
        self._minutes = int(time.time()%86400)%3600//60
        self._hour    = int(time.time()%86400)//3600

    def __str__(self) -> str:
        return str(self._hour) + ':' + str(self._minutes) + ':' + str(self._seconds)

    def hour(self):
        return self._hour
    
    def minute(self):
        return self._minutes
    
    def second(self):
        return self._seconds


now = dayTime3()
print(now)
