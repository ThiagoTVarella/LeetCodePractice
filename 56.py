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



################### Variant

def check_overlap(i1,i2):
    if i1[0] < i2[0]:
        return i1[1] >= i2[0]
    else:
        return i2[1] >= i1[0]

def merge(i1,i2):
    return [min(i1[0],i2[0]),max(i1[1],i2[1])]

def func(a,b):

    if not a: return b
    if not b: return a

    a = sorted(a)
    b = sorted(b)

    ia = 0
    ib = 0

    curr = None
    merged = []

    while ia < len(a) and ib < len(b):
        i1 = a[ia]
        i2 = b[ib]

        if i1[0] < i2[0]:
            interval = i1
            ia += 1
        else:
            interval = i2
            ib += 1

        if not merged: merged.append(interval)
        elif check_overlap(merged[-1],interval): merged[-1] = merge(merged[-1],interval)
        else: 
            merged.append(interval)

    remaining = a[ia:] + b[ib:]
    for interval in remaining:
        if check_overlap(merged[-1],interval):
            merged[-1] = merge(merged[-1],interval)
        else:
            merged.append(interval)

    return merged

a = [[1,5], [10,14], [16,18]]
b = [[2,6], [8,10], [11,20]]
print(func(a,b))

    