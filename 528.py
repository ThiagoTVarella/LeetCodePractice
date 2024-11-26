import random
import bisect

# [2,3]
# [0,2,5]

# [1,2,3,4,5]

class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sum = [0]
        for weight in w:
            self.prefix_sum.append(self.prefix_sum[-1]+weight)
        self.max = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        x = random.randint(1,self.max)
        # ind = bisect.bisect_left(self.prefix_sum,x)
        # return ind-1
        
        lo = 0
        hi = len(self.prefix_sum)-1

        while lo < hi:
            mi = lo + (hi-lo)//2

            if self.prefix_sum[mi] == x:
                return mi-1
            
            if self.prefix_sum[mi] < x:
                lo = mi+1
            else:
                hi = mi
        
        return lo-1

    # lo hi
    #    x
    # [0,1,4,5]
    # x = [1,2,3,4,5]
    # 

    #     self.cumsum = [0]
    #     for weight in enumerate(w):
    #         self.cumsum.append(self.cumsum[-1] + weight)
    #     self.max = self.cumsum[-1]

    #     # 0 3 17 18 25

    # def pickIndex(self) -> int:
    #     r = random.random()*self.max
    #     # pos = bisect.bisect_left(self.cumsum,r)-1
        
    #     left = 0
    #     right = len(self.cumsum)-1
    #     while left < right:
    #         mid = left + (right-left)//2 # mid is 0
            
    #         if self.cumsum[mid] < r:
    #             left = mid+1
    #         elif self.cumsum[mid] >= r:
    #             right = mid # right is 1, left is 0

    #     return left-1