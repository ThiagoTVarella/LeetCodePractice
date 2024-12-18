class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        lo = 0
        hi = len(arr)

        while lo < hi:
            mid = lo + (hi-lo)//2 

            if k <= arr[mid]-mid-1:
                hi = mid
            else:
                lo = mid+1

        return k + lo




















        # lo = 0
        # hi = len(arr)-1

        # while lo < hi:
        #     mi = lo + (hi-lo)//2

        #     if arr[mi] - mi - 1 >= k:
        #         hi = mi
        #     else:
        #         lo = mi+1

        # print(lo)

        # if arr[lo] - lo - 1 < k:
        #     return len(arr) + k
        # if lo == 0:
        #     return k

        # return lo + k



# [2,3,6,7,10]
# [1,1,3,3,5]
