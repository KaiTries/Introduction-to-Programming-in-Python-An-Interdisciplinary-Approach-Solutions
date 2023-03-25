    #genome sketching
from instream import InStream
import stdarray
from vector import Vector

class Genome:

    def __init__(self,string):
        self._gene = string
        self._hash = self.hash()



    def _sketch(self,k):
        count = stdarray.create1D(4**k,0)
        for i in range(len(self._gene) - k):
            kgram = self._gene[i:i + k]
            count[self.hash(kgram)] += 1
        vector = Vector(count)
        return count



    def sketch(self,k):
        count = stdarray.create1D(4**k,0)
        for i in range(len(self._gene) - k):
            kgram = self._gene[i:i + k]
            count[self.hash(kgram)] += 1
        vector = Vector(count)
        return vector.direction()

    def similarTo(self,other,k):
        vector = self.sketch(k)
        vector_other = other.sketch(k)
        return vector.dot(vector_other)

    def numberOf(self,string):
        k = len(string)
        wanted = self.hash(string)
        count = 0
        for i in range(len(self._gene) - k):
            kgram = self._gene[i:i + k]
            if self.hash(kgram) == wanted:
                count += 1
        return count

    def hash(self,kgram=''):
        if kgram == '':
            kgram = self._gene
        check = ['A','C','G','T']
        if not all([codon in check for codon in kgram]):
            raise Exception('not valid kgram')
        n = len(kgram)
        nums = ''
        for i in range(n):
            if kgram[i] == 'A':
                nums += '0'
            if kgram[i] == 'C':
                nums += '1'
            if kgram[i] == 'G':
                nums += '2'
            if kgram[i] == 'T':
                nums += '3'
        quarternal = nums[::-1]
        decimal = 0
        for i in range(len(quarternal)):
            decimal += int(quarternal[i]) * 4**(i)
        return decimal

    def unhash(self,decimal):
        d = decimal
        base4 = str(d%4)
        while d > 0:
            d = d//4
            x = d%4
            base4 = base4 + str(x)
        genome = ''
        for i in range(len(base4)):
            if base4[i] == '0':
                genome += 'A'
            if base4[i] == '1':
                genome += 'C'
            if base4[i] == '2':
                genome += 'G'
            if base4[i] == '3':
                genome += 'T'
        return genome[::-1]



input = InStream('genome.txt')
DNA = input.readAll()
DNA = Genome(DNA)
a = DNA

input = InStream('genome copy.txt')
DNA = input.readAll()
DNA = Genome(DNA)
b = DNA

print(a.similarTo(b,2))

print(b._sketch(2))