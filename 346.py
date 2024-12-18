from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque([])
        self.curr_size = 0
        self.curr_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.curr_sum += val
        if self.curr_size == self.size:
            self.curr_sum -= self.queue.popleft()
        else:
            self.curr_size += 1

        return self.curr_sum/self.curr_size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# movingAverage = MovingAverage(3)
# print(movingAverage.next(1))
# print(movingAverage.next(10))
# print(movingAverage.next(3))
# print(movingAverage.next(5))
