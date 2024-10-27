class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        numscopy = nums.copy()
        lentot = len(nums)
        for i in range(len(numscopy)):
            if numscopy[lentot-i-1] == val:
                nums.pop(lentot-i-1)
            else:
                k += 1
        return k
