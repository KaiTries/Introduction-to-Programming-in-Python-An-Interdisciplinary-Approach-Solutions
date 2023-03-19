# Accept string fileName and integer fieldCount as command-line
# arguments. Split the file whose name is fileName.csv, by field,
# into fieldCount+1 files named fileName1.txt, fileName2.txt, etc.
import sys
from instream import InStream
from outstream import OutStream
import stdarray

DELIM = ','


delimiterString = sys.argv[1]

# Create the input stream.
inputs = len(sys.argv[2:])
Inputlist = stdarray.create1D(inputs,)
for i in range(2,inputs+2):
    x = InStream(sys.argv[i])
    Inputlist[i-2]= x

#cleanup data 




#we now have a list of all the input files
#now we need to put them all into a single file
#and each line will be file + file2 etc. values being seperated by the delimiter string
# Create output streams.
OUTPUT = OutStream('date,close,volume.txt')

while Inputlist[0].hasNextLine():
    lines = []
    for i in range(len(Inputlist)):
        x = Inputlist[i].readLine()
        lines += [x]
        line = delimiterString.join(lines)
    OUTPUT.writeln(line)



