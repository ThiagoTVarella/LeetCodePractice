import heapq

class MedianFinder:

    def __init__(self):
        self.h_small = []
        self.h_large = []

    def fix_sizes(self):
        if len(self.h_small) < len(self.h_large)-1:
            elem = heapq.heappop(self.h_large)
            heapq.heappush(self.h_small, -elem)
        elif len(self.h_small) > len(self.h_large)+1:
            elem = -heapq.heappop(self.h_small)
            heapq.heappush(self.h_large, elem)

    def addNum(self, num: int) -> None:

        if not self.h_small and not self.h_large:
            self.h_small.append(-num)
        elif self.h_small and not self.h_large:
            if -self.h_small[0] <= num:
                self.h_large.append(num)
            else:
                self.h_large.append(-self.h_small[0])
                self.h_small[0] = -num
        elif self.h_large and not self.h_small:
            if -self.h_large[0] >= num:
                self.h_small.append(-num)
            else:
                self.h_small.append(-self.h_large[0])
                self.h_large[0] = num
        
        elif num < -self.h_small[0]:
            heapq.heappush(self.h_small, -num)
        else:
            heapq.heappush(self.h_large, num)

        self.fix_sizes()

        # print(self.h_small, self.h_large)
            

    def findMedian(self) -> float:
        totlen = len(self.h_small) + len(self.h_large)

        if totlen%2 and len(self.h_small) < len(self.h_large):
            return self.h_large[0]
        elif totlen%2 and len(self.h_small) > len(self.h_large):
            return -self.h_small[0]
        else:
            return (self.h_large[0] - self.h_small[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()