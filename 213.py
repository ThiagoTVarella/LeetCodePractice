class Solution:

    def lin(self, nums):

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        best = [nums[0],max(nums[0],nums[1])]

        for elem in nums[2:]:
            best.append(max(best[-1],best[-2]+elem))

        return best[-1]

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])        
        
        return max(self.lin(nums[1:]),self.lin(nums[:-1]))