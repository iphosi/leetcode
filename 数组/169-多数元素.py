from typing import List


# Boyer-Moore 投票算法
# count: 候选众数相较于其他元素多出现的次数


def majorityElement(nums: List[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
