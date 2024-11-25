from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        # counter_s = Counter(s)

        c = {}
        new_s = ''

        for ch in s:
            if ch in order:
                if ch in c: c[ch] += 1
                else: c[ch] = 1
            else: new_s += ch

        print(new_s)

        for ch in order:
            if ch in c:
                while c[ch] > 0:
                    c[ch] -= 1
                    new_s += ch 
                del c[ch]

        return new_s