class Solution:
    def validPalindrome(self, s: str) -> bool:

        # Initialize two pointers
        beg = 0
        end = len(s) - 1

        # Iterate pointers checking if equal
        while end > beg:
            # Handle skip case checking both sides
            if s[beg] != s[end]:
                string1 = s[beg:end]
                string2 = s[beg+1:end+1]
                if string1 == string1[::-1] or string2 == string2[::-1]:
                    return True
                else:
                    return False

            # Move to next pair        
            beg += 1
            end -= 1

        return True