#Describe what happens if you try to execute useargument.py with each of the following command lines:

#below the code for useargument.py

#import stdio
#import sys
#
#stdio.write('Hello, ')
#stdio.write(sys.argv[1])
#stdio.writeln(' What is your name? ')



#a. python useargument.py python
    #Hello, python What is your name? 
#b. python useargument.py @!&^%
    #not a valid python identifier 
#c. python useargument.py 1234
    #Hello, 1234 What is your name?
#d. python useargument Bob
    #C:\Python310\python.exe: can't open file '...\MyCode\\Python\\userargument': [Errno 2] No such file or directory
#e. useargument.py Bob
    #not a valid python identifier
#f. python useargument.py Alice Bob
    #Hello, Alice What is your name? 
    #Bob is forgotten