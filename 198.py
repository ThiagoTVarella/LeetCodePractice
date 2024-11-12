class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0],nums[1])

        best = [nums[0],max(nums[0],nums[1])]

        i = 2
        while i < n:
            best.append(max(best[i-1],best[i-2]+nums[i]))
            i += 1
        
        return best[-1]