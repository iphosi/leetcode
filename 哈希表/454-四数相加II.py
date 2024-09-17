from typing import List
from collections import defaultdict


def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    count_dict = defaultdict(int)
    count = 0

    for num1 in nums1:
        for num2 in nums2:
            count_dict[num1 + num2] += 1

    for num3 in nums3:
        for num4 in nums4:
            try:
                count += count_dict[0 - num3 - num4]
            except:
                continue

    return count
