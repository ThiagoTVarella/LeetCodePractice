class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        rep = 0
        for i,elem in enumerate(nums[:-1]):
            if elem == nums[i+1]:
                nums[i] = None
                rep += 1
        k = len(nums) - rep
        
        pointer_end = 0
        pointer_curr = 0
        
        while pointer_end < len(nums):
            while nums[pointer_end] == None:
                pointer_end += 1
            nums[pointer_curr] = nums[pointer_end]
            pointer_curr += 1
            pointer_end += 1
        
        return k
 



