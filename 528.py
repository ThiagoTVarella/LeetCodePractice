import random
import bisect

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix.append(prefix_sum)

    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()
        # target = random.randint(1, self.prefix_sums[-1])
        # run a binary search to find the target zone

        # low, high = 0, len(self.prefix)
        # while low < high:
        #     mid = low + (high - low) // 2
        #     if target > self.prefix[mid]:
        #         low = mid + 1
        #     else:
        #         high = mid

        low = bisect_left(self.prefix, target)
        return low