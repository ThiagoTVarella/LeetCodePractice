class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = nums[0]
        count1 = 0

        if len(nums) == 1:
            return nums

        cand2 = nums[1]
        count2 = 0

        for elem in nums:
            if elem == cand1:
                count1 += 1
            elif elem == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = elem
                count1 = 1
            elif count2 == 0:
                cand2 = elem
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        for elem in nums:
            if elem == cand1:
                count1 += 1
            elif elem == cand2:
                count2 += 1

        result = []
        threshold = int(len(nums)/3)
        if count1 > threshold:
            result.append(cand1)
        if count2 > threshold:
            result.append(cand2)

        return result

# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 2
# 5 -> 2
# 6 -> 3