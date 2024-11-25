# import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1,-1]

        l,r = 0,len(nums)-1

        # [5,7,7,8,8,10]
        # target = 8
        # l at 5, r at 10
        # m at 7
        # l at 8
        # m at 8

        while l+1 < r:
            mid = l + (r-l)//2
            # print(l,r,mid, nums[l],nums[r],nums[mid])

            if nums[mid] < target:
                l = mid+1
            else:
                r = mid

        if nums[l] == target:
            leftmost = l
        else:
            leftmost = r
 
        l,r = 0,len(nums)-1

        while l+1 < r:
            mid = l + (r-l)//2

            if target < nums[mid]:
                r = mid-1
            else:
                l = mid

        if len(nums)==1:
            rightmost = 0
            leftmost = 0
        elif len(nums) == 2:
            if nums[1] == target:
                rightmost = 1
            else:
                rightmost = 0

            if nums[0] == target:
                leftmost = 0
            else:
                leftmost = 1

        else:
            if nums[r] == target:
                rightmost = r
            else:
                rightmost = l

        if nums[leftmost] == target and nums[rightmost] == target:
            return [leftmost,rightmost]
        else:
            return [-1,-1]


















        # if 1 <= bisect.bisect_right(nums,target) <= len(nums):
        #     right = bisect.bisect_right(nums,target)-1
        # else:
        #     right = bisect.bisect_right(nums,target)

        # left = bisect.bisect_left(nums,target)

        # if left < len(nums) and nums[left] == target and nums[right] == target:
        #     return [left,right]
        # else:
        #     return [-1,-1]