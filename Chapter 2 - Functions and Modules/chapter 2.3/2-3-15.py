#binary representation
import stdio

n = 10

# Write to standard output the binary representation of n.

def convert(n):
    if n == 0:
        return
    convert(n // 2)
    stdio.write(n % 2)
convert(10)
stdio.writeln()
