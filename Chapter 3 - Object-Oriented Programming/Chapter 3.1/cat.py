import sys
from instream import InStream
from outstream import OutStream

# Copy files or web pages whose names are given by sys.argv[1:n-2]
# to the file whose name is given by sys.argv[n-1].

WEBSITE = 'https://meteo.search.ch/9445'
outFilename = 'out.txt'
outstream = OutStream(outFilename)

instream = InStream(WEBSITE)
s = instream.readAll()
outstream.writeln(s)