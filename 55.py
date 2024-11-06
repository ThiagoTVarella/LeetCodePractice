class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # go through the array backwards, save 1 if can reach the next 1, 0 if not
        # keep position of the last 1 seen
        # check if position + element < last 1 seen 
        bools = [True]
        last = len(nums)-1
        i = len(nums)-2
        while i >= 0:
            elem = nums[i]
            if i + elem >= last:
                bools.append(True)
                last = i
            else:
                bools.append(False)

            i -= 1

        return bools.pop()
