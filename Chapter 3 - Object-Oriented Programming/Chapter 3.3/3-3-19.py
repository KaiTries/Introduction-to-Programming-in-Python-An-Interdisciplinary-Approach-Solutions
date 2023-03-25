#genome


#A C G T


#addcodon
#baseat
#ispotentialgenome



class genomeString:

    def __init__(self,string: str=''):
        self._data = string

    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        return self._data
    
    def __getitem__(self, i):
        return self._data[i]

    def addCodon(self,c):
        self._data += c

    def baseAt(self, i):
        return self._data[i]
    
    def isPotentialGene(self):
        # number of bases is a multiple of 3
        if (len(self) % 3) != 0: return False
        # starts with start codon
        if not self.startswith('ATG'): return False
        # no intervening stop codons
        for i in range(len(self) - 3):
            if i % 3 == 0:
                if self[i:i+3] == 'TAA': return False
                if self[i:i+3] == 'TAG': return False
                if self[i:i+3] == 'TGA': return False
        # ends with a stop codon
        if self.endswith('TAA'): return True
        if self.endswith('TAG'): return True
        if self.endswith('TGA'): return True
        return False


    

class genomeArray:


    def __init__(self, array: list=[]):
        self._data = array

    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)
    
    def __getitem__(self, i):
        return self._data[i]
    

    def baseAt(self, i):
        return self._data[i]

    def addCodon(self, i):
        self._data += [i]

    def isPotentialGene(self):
        _stringify = self._data[:]
        _string = ''
        for i in range(len(_stringify)):
            _string += self.baseAt(i)
        # number of bases is a multiple of 3
        if (len(_string) % 3) != 0: return False
        # starts with start codon
        if not _string.startswith('ATG'): return False
        # no intervening stop codons
        for i in range(len(_string) - 3):
            if i % 3 == 0:
                if _string[i:i+3] == 'TAA': return False
                if _string[i:i+3] == 'TAG': return False
                if _string[i:i+3] == 'TGA': return False
        # ends with a stop codon
        if _string.endswith('TAA'): return True
        if _string.endswith('TAG'): return True
        if _string.endswith('TGA'): return True
        return False

class genomeBinary:


    def __init__(self, array: list=[]):
        self._bools = array

    def __str__(self) -> str:
        return str(self._bools)
    
    def __getitem__(self, i):
        return self._bools[i]
    
    def addCodon(self, c):
        if c == 'A' :
            c = [0,0]
            self._bools += [c]
        if c == 'C' :
            c = [0,1]
            self._bools += [c]
        if c == 'G' :
            c = [1,0]
            self._bools += [c]
        if c == 'T' :
            c = [1,1]
            self._bools += [c]

    def baseAt(self, i):
        c = self[i]
        if c == [0,0] :
            c = 'A'
        if c == [0,1] :
            c = 'C'
        if c == [1,0] :
            c = 'G'
        if c == [1,1] :
            c = 'T'
        return c

    def isPotentialGene(self):
        _stringify = self._bools[:]
        _string = ''
        for i in range(len(_stringify)):
            _string += self.baseAt(i)
        # number of bases is a multiple of 3
        if (len(_string) % 3) != 0: return False
        # starts with start codon
        if not _string.startswith('ATG'): return False
        # no intervening stop codons
        for i in range(len(_string) - 3):
            if i % 3 == 0:
                if _string[i:i+3] == 'TAA': return False
                if _string[i:i+3] == 'TAG': return False
                if _string[i:i+3] == 'TGA': return False
        # ends with a stop codon
        if _string.endswith('TAA'): return True
        if _string.endswith('TAG'): return True
        if _string.endswith('TGA'): return True
        return False

test = genomeArray()
print(test)
test.addCodon('A')
test.addCodon('T')
test.addCodon('G')
test.addCodon('A')
test.addCodon('C')
test.addCodon('C')
test.addCodon('T')
test.addCodon('G')
test.addCodon('A')
print(test)
print(test.baseAt(2))
print(test.isPotentialGene())