class Solution:
    def isPalindrome(self, s: str) -> bool:
        i_beg = 0
        i_end = len(s)-1

        finish = False

        while i_beg < i_end and not finish:
            # Read relevant chars
            beg_char = s[i_beg]
            end_char = s[i_end]

            # Check if satisfy conditions
            while not beg_char.isalnum():
                i_beg += 1
                if i_beg < len(s):
                    beg_char = s[i_beg]
                else:
                    finish = True
                    break

            while not end_char.isalnum():
                i_end -= 1
                if i_end >= 0:
                    end_char = s[i_end]
                else:
                    finish = True
                    break
                
            if not beg_char.islower():
                beg_char = beg_char.lower()
            if not end_char.islower():
                end_char = end_char.lower()

            if beg_char != end_char and not finish:
                return False

            i_beg += 1
            i_end -= 1

        return True

# Two pointers
# .isalnum(), if not skip
# .islower(), if not .lower()
# if ==, if not False
# return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         filtered = ''.join(c.lower() for c in s if c.isalnum())
#         return filtered == filtered[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Converts s to lowercase without punctuation marks
        Check if s is equal to s reverse
        Time: O(2N)
        Space: O(N)
        N is the size of s
        """
        
        sl = ''
        for ch in s:
            if ch.isalnum():
                sl += ch.lower()

        return sl == sl[::-1]

        # joint = ''
        # for elem in s:
        #     if elem.isalnum():
        #         joint += elem.lower()
            
        # return joint == joint[::-1]