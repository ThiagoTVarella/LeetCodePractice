class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        counter_1 = m-1
        counter_2 = n-1
        pointer = m+n-1

        while pointer >= 0:

            if counter_1 >= 0 and counter_2 >= 0:
                if nums1[counter_1] >= nums2[counter_2]:
                    nums1[pointer] = nums1[counter_1]
                    counter_1 -= 1
                else:
                    nums1[pointer] = nums2[counter_2]
                    counter_2 -= 1

            elif counter_1 < 0 and counter_2 >= 0:
                nums1[pointer] = nums2[counter_2]
                counter_2 -= 1
            
            pointer -= 1
            

     





















        # pt1 = m-1
        # pt2 = n-1
        # pt = m+n-1

        # while pt >= 0:
            
        #     if pt1 < 0:
        #         nums1[pt] = nums2[pt2]
        #         pt2 -= 1
        #         pt -= 1

        #     elif pt2 < 0:
        #         nums1[pt] = nums1[pt1]
        #         pt1 -= 1
        #         pt -= 1

        #     elif nums1[pt1] >= nums2[pt2]:
        #         nums1[pt] = nums1[pt1]
        #         pt1 -= 1
        #         pt -= 1

        #     else:
        #         nums1[pt] = nums2[pt2]
        #         pt2 -= 1
        #         pt -= 1



        # #[1,0] [1]




