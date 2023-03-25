
#-----------------------------------------------------------------------
# cat.py
#-----------------------------------------------------------------------

import sys
from instream import InStream
from outstream import OutStream

# Copy files or web pages whose names are given by sys.argv[1:n-2]
# to the file whose name is given by sys.argv[n-1].

inFilenames = 'https://en.wikipedia.org/wiki/Main_Page'
outFilename = 'output.txt'
outstream = OutStream(outFilename)

instream = InStream('https://en.wikipedia.org/wiki/2675_Tolkien')
s = instream.readAllStrings()
outstream.write(s)

#-----------------------------------------------------------------------
