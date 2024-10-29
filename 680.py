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

def check_palindrome(s: str) -> bool:
    return s == s[::-1]

def valid_palindrome(s: str) -> bool:
    beg_pointer = 0
    end_pointer = len(s)-1

    if check_palindrome(s):
        return True
    while beg_pointer < end_pointer:
        if s[beg_pointer] == s[end_pointer]:
            beg_pointer += 1
            end_pointer -= 1
        else:
            string1 = s[beg_pointer:end_pointer]
            string2 = s[beg_pointer+1:end_pointer+1]
            if check_palindrome(string1) or check_palindrome(string2):
                return True
            else:
                return False

print(valid_palindrome('geeeeeea'))