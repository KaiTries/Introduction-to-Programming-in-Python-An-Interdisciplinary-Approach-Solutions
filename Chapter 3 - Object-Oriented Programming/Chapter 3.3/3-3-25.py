#calendar

#dates

from datetime import date
class calenderIter:
    def __init__(self, calender):
        self._calender = calender._calender
        self._calender_size = len(self._calender)
        self._current_index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._current_index < self._calender_size:
            member = self._calender[self._current_index] 
            self._current_index += 1
            return member
        raise StopIteration


class calender:

    def __init__(self):
        self._calender = []

    def append(self, x):
        if len(self._calender) < 1:
            self._calender += [x]
        else:
            for i in range(len(self._calender)):
                if x < self._calender[i]:
                    self._calender = self._calender[:i] + [x] + self._calender[i:]
                    return
            self._calender += [x]

    def __str__(self):
        for i in range(len(self._calender)):
            print(self._calender[i])
        return ''
    
    def currentAppointments(self):
        for i in range(len(self._calender)):
            print(self._calender[i])

    def __iter__(self):
        return calenderIter(self)

class Appointment:

    def __init__(self,year,month,day,description=''):
        self._year = year
        self._month = month
        self._day = day
        self._desc = description
        self._data = date(self._year,self._month,self._day)

    def __str__(self) -> str:
        return str(self._data) + ', ' + str(self._desc)
    
    def __lt__(self,other):
        if self._data < other._data: return True
        else: return False
    
    def __gt__(self,other):
        if self._data > other._data: return True
        else: return False

    def __eq__(self,other):
        if self._data == other._data: return True
        else: return False


    def addTo(self,calender: calender):
        if self in calender: return print('date already booked')
        else: calender.append(self)



C = calender()
a = Appointment(2023,1,10,'doctor')
b = Appointment(2023,4,10,'test')
c = Appointment(2023,2,10,'test')
d = Appointment(2023,10,10,'test')
a.addTo(C)
print(C)

C.append(b)
print(C)
c.addTo(C)
print(C)
d.addTo(C)
print(C)