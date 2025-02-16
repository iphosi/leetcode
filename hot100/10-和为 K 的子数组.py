from typing import List
from collections import defaultdict


def subarraySum(nums: List[int], k: int) -> int:
    # 考虑以 i 结尾的和为 k 的连续子数组个数时，只要统计到 i 为止，有多少个前缀和为 prefix − k 即可
    count = 0
    prefix = 0
    prefix_dict = defaultdict(int)
    prefix_dict[0] = 1

    for i in range(len(nums)):
        prefix += nums[i]
        if prefix - k in prefix_dict:
            count += prefix_dict[prefix - k]
        prefix_dict[prefix] += 1

    return count
