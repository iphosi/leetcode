import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findTopK(nums, k, 0, len(nums) - 1)

    def findTopK(self, nums, k, start, end):
        rand_idx = random.randint(start, end)
        nums[start], nums[rand_idx] = nums[rand_idx], nums[start]

        p = start
        j = start + 1
        for i in range(start + 1, end + 1):
            if nums[i] >= nums[p]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        nums[p], nums[j - 1] = nums[j - 1], nums[p]

        if j == k:
            return nums[k - 1]
        elif j > k:
            return self.findTopK(nums, k, start, j - 2)
        else:
            return self.findTopK(nums, k, j, end)