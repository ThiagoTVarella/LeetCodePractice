class Solution:

    def myPow(self,x,n):

        if n < 0:
            return 1/self.myPow(x,-n)

        if n == 0:
            return 1

        power = x
        i = 1
        while 2*i <= n:
            power *= power
            i *= 2

        return power*self.myPow(x,n-i)

    #     if n == 0: return 1
    #     if n == 1: return x
    #     if n == 2: return x*x
    #     if n < 0: return 1/self.myPow(x,-n)

    #     p = x
    #     next_expo = 2

    #     while next_expo <= n:
    #         p *= p
    #         next_expo *= 2

    #     expo = next_expo//2
    #     return p*self.myPow(x,(n-expo))

# from functools import cache

    # @cache
    # def binaryPow(self,x,n):

    #     if n == 1: return x

    #     if n == 0: return 1

    #     if x == 0: return 0

    #     if n < 0: return 1/self.binaryPow(x,-n)
        
    #     if not n%2:
    #         return self.binaryPow(x,n//2)*self.binaryPow(x,n//2)
    #     else:
    #         return self.binaryPow(x,n//2)*self.binaryPow(x,1+(n//2))


    # def myPow(self, x: float, n: int) -> float:

    #     return self.binaryPow(x,n)
