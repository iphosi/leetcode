from collections import Counter
import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count_dict = Counter(nums)

    heap = []
    for num, count in count_dict.items():
        heapq.heappush(heap, [count, num])
        if len(heap) > k:
            heapq.heappop(heap)

    return [item[1] for item in heap]
