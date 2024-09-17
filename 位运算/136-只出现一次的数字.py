from typing import List
from functools import reduce


# 任何数和 0 做异或运算，结果仍然是原来的数。
# 任何数和其自身做异或运算，结果是 0。
# 异或运算满足交换律和结合律。


def singleNumber(nums: List[int]) -> int:
    result = nums[0]

    for i in range(1, len(nums)):
        result = result ^ nums[i]

    return result


def singleNumber(nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)
