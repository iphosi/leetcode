from typing import List


def runningSum(nums: List[int]) -> List[int]:
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    return prefix
