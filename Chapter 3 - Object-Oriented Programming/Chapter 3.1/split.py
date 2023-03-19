#-----------------------------------------------------------------------
# split.py
#-----------------------------------------------------------------------

import sys
import stdarray
from instream import InStream
from outstream import OutStream

#-----------------------------------------------------------------------

# Accept string fileName and integer fieldCount as command-line
# arguments. Split the file whose name is fileName.csv, by field,
# into fieldCount+1 files named fileName1.txt, fileName2.txt, etc.

DELIM = ','

fileName = sys.argv[1]
fieldCount = int(sys.argv[2])

# Create the input stream.
inStream = InStream(fileName + '.csv')

# Create output streams.
outStreams = stdarray.create1D(fieldCount)
for i in range(fieldCount):
    file = OutStream(fileName + str(i) + '.txt')
    outStreams[i] = file

# Read lines from the input stream and write them to the
# output stream.
while inStream.hasNextLine():
    line = inStream.readLine()
    fields = line.split(DELIM)
    for i in range(fieldCount):
        outStreams[i].writeln(fields[i])