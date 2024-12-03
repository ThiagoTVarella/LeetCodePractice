class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        count = 0

        for elem in nums:
            if elem == cand:
                count += 1
            else:
                count -= 1

            if count == 0:
                cand = elem
                count = 1

        return cand



no need to introduce the next speaker