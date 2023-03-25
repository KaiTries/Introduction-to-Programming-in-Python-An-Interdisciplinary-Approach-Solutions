

List = ["fl","flow","flight"]
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs: 
            return ''
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and first[i] == last[i]:
            i += 1
        return first[:i]

a = 0
print(Solution.longestCommonPrefix(a,List))

a = ["flx","ftt","flight"]

a.sort()
print(a)