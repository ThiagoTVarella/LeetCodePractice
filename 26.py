# 1 1 1 1 1 2 2 2 3 4

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 0

        lo = elem_index = 0
        k = 0

        while elem_index < len(nums):
            k += 1

            hi = len(nums)
            while lo < hi:
                
                mid = lo + (hi-lo)//2

                if nums[mid]>nums[elem_index]:
                    hi = mid
                else:
                    lo = mid+1
            
            nums[last] = nums[elem_index]
            last += 1
            elem_index = lo

        return k
        


        # # remember last element seen
        # last = nums[0]
        # # have stack of empty indeces
        # qu = deque()
        # # have counter of repeated elements
        # rep = 0
        # # iterate through 
        # i = 1
        # while i < len(nums):
        #     elem = nums[i]
        #     if elem == last: 
        #         rep += 1
        #         qu.append(i)
        #     else:
        #         last = elem
        #         if qu:
        #             pos = qu.popleft()
        #             nums[pos] = last
        #             qu.append(i)

        #     i += 1 # 2

        # return len(nums)-rep



