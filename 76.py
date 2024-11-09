class Solution:
    def minWindow(self, s: str, t: str) -> str:
            
        # Creating counter for t
        # Creating counter for substring of s only with elements inside of t_counter
        # Create pointers for the substring of s (to easily remember len)

        hashmap = {}
        begin = 0
        end = 0
        head = 0
        subleb = float('inf')
        counter = len(t)

        # create hashmap
        for char in t:
            hashmap[char] = hashmap.get(char,0) + 1

        while end < len(s):

            if s[end] in hashmap:

                hashmap[s[end]] -= 1

                if hashmap[s[end]] >= 0:
                    counter -= 1
            
            # while check
            while counter == 0:
                
                if subleb > end-begin+1:
                    subleb = end-begin+1
                    head = begin

                if s[begin] in hashmap:
                    hashmap[s[begin]] += 1

                    if hashmap[s[begin]] > 0:
                        counter += 1
                begin += 1

            end += 1


        return s[head:head+subleb] if subleb != float('inf') else ''
