import stdio


def duplicate(s):
    t = s + s

s = 'Hello'
s = duplicate(s)
t = 'bye'
t = duplicate(duplicate(duplicate(t)))


stdio.writeln(s + t)

#Traceback (most recent call last):
#  MyCode\Python\chapter 2.1\2-1-9.py", line 10, in <module>
#    t = duplicate(duplicate(duplicate(t)))
#  MyCode\Python\chapter 2.1\2-1-9.py", line 5, in duplicate
#    t = s + s
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
