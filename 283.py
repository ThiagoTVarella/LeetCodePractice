class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                n -= 1
            else:
                i += 1

from typing import List

def move_zeroes(nums: List[int]) -> None:
    
    # create pointers
    beg_pointer = 0
    end_pointer = len(nums)-1

    while beg_pointer < end_pointer:
        if nums[beg_pointer] == 0:
            nums.pop(beg_pointer)
            nums.append(0)
            end_pointer -= 1

        else:
            beg_pointer += 1

num = [0,1,3,0,3]
move_zeroes(num)
print(num)
