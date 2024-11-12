from functools import cache

class Solution:

    @cache
    def binaryPow(self,x,n):

        if n == 1: return x

        if n == 0: return 1

        if x == 0: return 0

        if n < 0: return 1/self.binaryPow(x,-n)
        
        if not n%2:
            return self.binaryPow(x,n//2)*self.binaryPow(x,n//2)
        else:
            return self.binaryPow(x,n//2)*self.binaryPow(x,1+(n//2))


    def myPow(self, x: float, n: int) -> float:

        return self.binaryPow(x,n)
