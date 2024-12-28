class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            left,right = i,i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count

# @cache 
# def check_palindrome(s):

#     if len(s) == 1:
#         return True

#     if len(s) == 2:
#         if s[0] == s[1]: return True
#         else: return False

#     if len(s) > 0 and s[0] == s[-1]:
#         if check_palindrome(s[1:-1]):
#             return True
#         else:
#             False 
#     else:
#         False

# class Solution:
#     def countSubstrings(self, s: str) -> int:

#         count = 0
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 if check_palindrome(s[i:j+1]):
#                     count += 1

#         return count