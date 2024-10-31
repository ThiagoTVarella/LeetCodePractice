class Solution:
    def climbStairs(self, n: int) -> int:
        # def memo_fibonacci(n, memo = {}):
        #     if n in memo:
        #         return memo[n]
        #     if n == 1:
        #         return 1
        #     elif n == 2:
        #         return 2
        #     memo[n] = memo_fibonacci(n-1,memo) + memo_fibonacci(n-2,memo) 
        #     return memo[n]
        # return memo_fibonacci(n)

        seq = [1,2]
        
        for i in range(2,n):
            seq.append(seq[i-2]+seq[i-1])
        
        return(seq[n-1])