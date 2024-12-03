class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix_mod = {0:-1}
        prev = 0
        for i,elem in enumerate(nums):
            # print(prefix_mod)
            curr_prefix = (prev + elem)%k
            if curr_prefix in prefix_mod and i - prefix_mod[curr_prefix] > 1:
                return True
            if curr_prefix not in prefix_mod:
                prefix_mod[curr_prefix] = i
            prev = curr_prefix

        return False
