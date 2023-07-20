from collections import Counter
  
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl=list(s)
        tl=list(t)
        for i in sl:
            if i not in tl:
                return False
            j=tl.index(i)
            tl=tl[j+1:]
        
        return True
        
        