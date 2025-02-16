from collections import deque
from typing import List


class MonoQueue:
    def __init__(self):
        self.data = deque()

    def front(self):
        return self.data[0]

    def push(self, val):
        # 单调递减队列
        while self.data and self.data[-1] < val:
            self.data.pop()

        self.data.append(val)

    def pop(self, val):
        # 比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出
        # 如果不相等，则说明该元素已经在 push 阶段被弹出
        if self.data and self.data[0] == val:
            self.data.popleft()


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    mono_queue = MonoQueue()
    result = []

    for i in range(k):
        mono_queue.push(nums[i])

    result.append(mono_queue.front())

    for i in range(k, len(nums)):
        mono_queue.pop(nums[i - k])
        mono_queue.push(nums[i])
        result.append(mono_queue.front())

    return result
