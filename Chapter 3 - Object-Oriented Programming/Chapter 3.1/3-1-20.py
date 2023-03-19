#filter that removes whitespace
#reads input and then outputs filtered
#try it with a in1.txt and out.txt
from instream import InStream
from outstream import OutStream



INPUT = InStream('in1.txt')


filtered = []
while INPUT.hasNextLine():
    sample = INPUT.readLine()
    sample = sample.strip()
    if len(sample) > 0:
        filtered += [sample]


filtered = '\n'.join(filtered)



OUTPUT = OutStream('out1.txt')
OUTPUT.write(filtered)