#Modify useargument.py to compose a program that takes three names and writes a proper sentence with the names in the reverse of the order they are given, 
#so that, for example, python usethree.py Alice Bob Carol writes the string 'Hi Carol, Bob, and Alice'.

import stdio
import sys

stdio.write('Hello, ')
stdio.write(sys.argv[3])
stdio.writeln('. What is your name? ')
stdio.write('Hello, ')
stdio.write(sys.argv[2])
stdio.writeln('. Nice to meet you. This is my collegue,')
stdio.write(sys.argv[1])    

#they are written in reverse order since the last argument is the first one in the list