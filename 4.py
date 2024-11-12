class Solution:

    # def condition(self,mid) -> bool:
    #     mid2 = self.k-(mid+1)-1
    #     if mid2 < 0 or mid2+1 >= len(self.nums2):
    #         return True
    #     if mid+1 >= len(self.nums1) or mid < 0:
    #         return True        
    #     return (self.nums1[mid] < self.nums2[mid2+1]) and (self.nums2[mid2] < self.nums1[mid+1])

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = (total + 1) // 2
        
        left, right = 0, n1
        
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half - mid1
            
            left1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            right1 = float('inf') if mid1 == n1 else nums1[mid1]
            left2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            right2 = float('inf') if mid2 == n2 else nums2[mid2]
            
            # Check if we found the correct partition
            if left1 <= right2 and left2 <= right1:
                # If total length is odd
                if total % 2:
                    return max(left1, left2)
                # If total length is even
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1