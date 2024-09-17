from typing import List
from collections import defaultdict
import heapq


# 对所有元素排序，时间复杂度为 O(nlog(n))
# 对 k 个元素排序，时间复杂度为 O(nlog(k))
# 定义一个大小为 k 的小顶堆，大小大于 k 时弹出元素，该元素为堆中的最小值
# 最终堆中剩余的元素即为前 k 大的元素

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count_dict = defaultdict(int)

    for num in nums:
        count_dict[num] += 1

    return sorted(
        list(count_dict.keys()),
        key=lambda key: count_dict[key]
    )[-k:]


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count_dict = defaultdict(int)

    for num in nums:
        count_dict[num] += 1

    heap = []

    for key, value in count_dict.items():
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            heapq.heappop(heap)

    return [key for _, key in heap]

