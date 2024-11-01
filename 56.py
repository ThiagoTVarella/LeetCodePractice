class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals = []
        intervals = sorted(intervals)
        pointer_left = 0
        n = len(intervals)

        # Iterate left pointer full
        while pointer_left < n:
            # Iterate right pointer until can't merge
            flag_continue = True
            pointer_right = pointer_left + 1
            aux_interval = intervals[pointer_left]
            while pointer_right < len(intervals) and flag_continue:
                
                interval2 = intervals[pointer_right]
                if interval2[0] <= aux_interval[1]:
                    # Merge
                    if interval2[1] > aux_interval[1]:
                        aux_interval[1] = interval2[1]

                    pointer_right += 1
                else:
                    flag_continue = False
            pointer_left = pointer_right
            new_intervals.append(aux_interval)
        
        return new_intervals

        # # Handle edge cases:
        # if not intervals:
        #     return []

        # # Sort the list 
        # intervals.sort()

        # # Define final list
        # merged = [intervals[0]]

        # # Iterate over elements
        # i = 1
        # while i < n:

        #     # Read the last 
        #     aux = merged[-1]
        #     current = intervals[i]

        #     # Compare with the next
        #     if current[0] < aux[1]:

        #         # Merge
        #         aux[1] = max(current[1],aux[1])



        #     else:

        #     i += 1




# Elie:
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         # sort by start idx
#         intervals = sorted(intervals)
#         out = []
#         # compare start idx
#         for curr in intervals:
#             if not out:
#                 out.append(curr)
#                 continue
#             prev = out.pop()
#             # start 1 > end 0: doesnt overlap!
#             if curr[0] > prev[1]:
#                 out.append(prev)
#                 out.append(curr)
#                 continue
#                 # dont overlap -> stage previous interval for output, move on to this one
#             # if start 1 >= start 0: overlaps!
#             if curr[0] >= prev[0]:
#                 end = max(curr[1], prev[1])
#                 out.append([prev[0], end])
#                 continue
#             # start 1 == end 0: endpoints match
#             if curr[0] == prev[1]:
#                 out.append([prev[0], curr[1]])
#                 continue

#         return out
