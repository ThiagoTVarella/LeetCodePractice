
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if len(arr) == k:
            return arr

        lo = 0
        hi = len(arr)-k

        while lo < hi:
            mid = lo + (hi-lo)//2

            if x-arr[mid] <= arr[mid+k]-x:
                hi = mid
            else:
                lo = mid+1

        return arr[lo:lo+k]


# [0,0,1,2,3,3,4,7,7,8]
# [5,5,4,3,2,2,1,2,2,3]

        # [1,2,3,4,5]
        # k = 4, x = 3 
        # find first m that  

# from bisect import bisect_left


        # lo = bisect_left(arr,x)
        # left, right = lo-1, lo
        # out = []

        # while k > 0:
        #     if left < 0:
        #         out.append(arr[right])
        #         right += 1
        #     elif right >= len(arr):
        #         out.append(arr[left])
        #         left -= 1
        #     elif abs(arr[left]-x) <= abs(arr[right]-x):
        #         out.append(arr[left])
        #         left -= 1
        #     else:
        #         out.append(arr[right])
        #         right += 1

        #     k -= 1
        
        # out.sort()
        # return out














# from collections import deque


# def is_left_closer(left,right,x,arr):
#     if abs(arr[left]-x) < abs(arr[right]-x):
#         return True
#     if abs(arr[left]-x) == abs(arr[right]-x) and left < right:
#         return True
#     return False

# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         """
#         sorted arr
#         int k and x
#         return k closest integers to x, sorted

#         e.g. [1,2,3,4,5], k = 4, x = 3
#         # output 1,2,3,4
#         e.g. [1,1,2,3,4,5], k = 4, x = -1
#         # output 1,1,2,3

#         # in O(log(n)) I can find the index that x would be.
#         # Then, I can have a pointer that goes to the right and one that goes to the left
#         # And compare element by element, until I have k elements

#         """

#         lo = 0
#         hi = len(arr)
#         while lo < hi:
#             mid = lo + (hi-lo)//2
#             if arr[mid] >= x:
#                 hi = mid
#             else:
#                 lo = mid+1
        
#         # lo is the first index with element equal or higher than x
#         right = lo
#         left = lo-1
#         out = deque([])
#         while k > 0 and left >= 0 and right < len(arr):
#             if is_left_closer(left,right,x,arr):
#                 out.appendleft(arr[left])
#                 left -= 1
#             else:
#                 out.append(arr[right])
#                 right += 1
#             k -= 1

#         while k > 0 and left >= 0:
#             out.appendleft(arr[left])
#             left -= 1
#             k -= 1

#         while k > 0 and right < len(arr):
#             out.append(arr[right])
#             right += 1
#             k -= 1

#         return list(out)