class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashm = {}
        
        for i,char in enumerate(s):
            if char not in hashm:
                if t[i] in hashm.values(): return False
                hashm[char] = t[i]
                
            else:
                if hashm[char] != t[i]: return False 

        return True