class Solution:
    def isPalindrome(self, x: int) -> bool:
        old_x = x
        new_x = 0
        while old_x > 0:
            new_x = new_x*10 + old_x%10
            old_x //= 10 

        return True if new_x == x else False
