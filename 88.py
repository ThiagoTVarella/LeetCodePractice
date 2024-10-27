class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            pass
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:             
            # Create pointers i_m and i_n as the last non-decreasing element of nums1 and nums2
            i_m = m-1
            i_n = n-1
            
            # Iterate over final version of nums1 with counter
            counter = m+n-1

            print(nums1, i_m, counter)
            print(nums2, i_n)

            while counter >= 0:
                # Compare elements im and in and store highest at position counter of nums1
                # Iterate pointer im or in depending on the highest element             
                
                if i_m >= 0 and i_n >= 0:
                    if nums1[i_m] >= nums2[i_n]:
                        nums1[counter] = nums1[i_m]
                        i_m -= 1
                    else:
                        nums1[counter] = nums2[i_n]
                        i_n -= 1
                elif i_m < 0 and i_n >= 0:
                    nums1[counter] = nums2[i_n]
                    i_n -= 1
                elif i_n < 0:
                    break
                counter -= 1