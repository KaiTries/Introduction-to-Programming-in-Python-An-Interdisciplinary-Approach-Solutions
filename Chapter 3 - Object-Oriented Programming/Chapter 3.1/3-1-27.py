#kama sutra cypher
from instream import InStream
import sys
import stdio
#two key strings as command line argument
#cypher table
#key strings must be of equal length and must have all letters that are used in standard input later on

#eg:
#THEQUICKBROWN
#FXJMPSVLAZYDG

#-> enocdes T to F and E to J etc. also vice versa!

#we take two arguments then get standard input
#we give the encoded message as standard ouput back

KEY1 = 'THEQUICKBROWN'
KEY2 = 'FXJMPSVLAZYDG'

message = stdio.readAll()
message = message.upper()
print(message)
#encoding
codedMessage = ''
for i in range(len(message)):
    if message[i] in KEY1:
        index = KEY1.find(message[i])
        codedMessage += KEY2[index]
    elif message[i] in KEY2:
        index = KEY2.find(message[i])
        codedMessage += KEY1[index]
    elif message[i] == ' ':
        codedMessage += ' '
    else:
        print("character not in keys")
print(codedMessage)




