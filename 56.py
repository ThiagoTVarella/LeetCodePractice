class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        intervals.sort()

        merged = [intervals[0]]

        for start,end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start,end])

        return merged

    # def check_overlap(self,a,b):
    #     # check if intervals a and b overlap, with a and b sorted
    #     if a[1] >= b[0]:
    #         return True
    #     else:
    #         return False

    # def merge_overlap(self,a,b):
    #     # merge overlapping intervals
    #     return [a[0],max([a[1],b[1]])]

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     sorted_intervals = sorted(intervals)
    #     merged = []

    #     pointer = 0
    #     while pointer < len(intervals)-1:
    #         curr_int = sorted_intervals[pointer]
    #         next_int = sorted_intervals[pointer+1]
    #         while self.check_overlap(curr_int, next_int):
    #             curr_int = self.merge_overlap(curr_int, next_int)
    #             pointer += 1
    #             if pointer < len(intervals)-1:
    #                 next_int = sorted_intervals[pointer+1]
    #             else:
    #                 break
    #         merged.append(curr_int)
    #         pointer += 1

    #     if pointer < len(intervals):
    #         curr_int = sorted_intervals[pointer]
    #         merged.append(curr_int)

    #     return merged

    