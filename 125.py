class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if s is a palindrome

        E.g. s = 'aBba' returns True

        Time complexity: O(n)
        Space complexity: O(1)
        """

        if len(s) <= 1:
            return True

        beg_pointer = 0
        end_pointer = len(s)-1

        while beg_pointer < end_pointer:
            
            while not s[beg_pointer].isalnum():
                beg_pointer += 1
            while not s[end_pointer].isalnum():
                end_pointer -= 1

            if s[beg_pointer].lower() != s[end_pointer].lower():
                return False
            
            beg_pointer += 1
            end_pointer -= 1

        return True

sol = Solution()
print(sol.isPalindrome('a1.B4.,/b1    a'))

        # i_beg = 0
        # i_end = len(s)-1

        # finish = False

        # while i_beg < i_end and not finish:
        #     # Read relevant chars
        #     beg_char = s[i_beg]
        #     end_char = s[i_end]

        #     # Check if satisfy conditions
        #     while not beg_char.isalnum():
        #         i_beg += 1
        #         if i_beg < len(s):
        #             beg_char = s[i_beg]
        #         else:
        #             finish = True
        #             break

        #     while not end_char.isalnum():
        #         i_end -= 1
        #         if i_end >= 0:
        #             end_char = s[i_end]
        #         else:
        #             finish = True
        #             break
                
        #     if not beg_char.islower():
        #         beg_char = beg_char.lower()
        #     if not end_char.islower():
        #         end_char = end_char.lower()

        #     if beg_char != end_char and not finish:
        #         return False

        #     i_beg += 1
        #     i_end -= 1

        # return True

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

        sl = ''.join(ch.lower() for ch in s if ch.isalnum())

        return sl == sl[::-1]

        # sl = ''
        # for ch in s:
        #     if ch.isalnum():
        #         sl += ch.lower()

