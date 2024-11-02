class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create the heap
        h = []
        heapq.heappush(h,nums[0])

        # Iterate through the array
        for elem in nums[1:]:
            # For every element I'll check if it's bigger than the smallest element to my minheap
            # If the heap is bigger than k, remove the smallest element
            if len(h) >= k:
                smallest = h[0]
                if elem > smallest:
                    heapq.heappop(h)
                    heapq.heappush(h,elem)
            else:
                heapq.heappush(h,elem)


        # After the iteration, return smallest element
        return h[0] # 2