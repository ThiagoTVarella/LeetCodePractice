import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Create a heap to keep track of the smallest element
        h = nums[0:k]

        # Make sure it's heapified
        heapq.heapify(h) # Linear time

        # Iterate through the array
        for elem in nums[k:]:
            
            # Fill the heap, maintaining the smallest element
            if elem > h[0]:
                heappushpop(h,elem)

        # Return the 0th element of the heap
        return h[0]