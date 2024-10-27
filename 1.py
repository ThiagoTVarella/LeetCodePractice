class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

	# Create hashmap
	# Iterate through the array
	# Check if difference is in hashmap
	# Add to the hashmap

	# Create hashmap
        hashmap = {}

	# Iterate over nums
        for elem_i in range(len(nums)):
            elem = nums[elem_i]

	    #Calculate difference
            diff = target-elem

	    # Check if difference is in hashmap
            if diff in hashmap:
                return [hashmap[diff],elem_i]

	    # If the difference is not yet in hashmap, add element to hashmap
            else:
                hashmap[elem] = elem_i