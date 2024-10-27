class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for elem_i in range(len(nums)):
            elem = nums[elem_i]
            diff = target-elem
            if diff in hashmap:
                return [hashmap[diff],elem_i]
            else:
                hashmap[elem] = elem_i

# Create hashmap
# Iterate through the array
# Check if difference is in hashmap
# Add to the hashmap