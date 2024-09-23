from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    i = 2

    while i < len(nums):
        if nums[i - 2] == nums[i - 1] == nums[i]:
            nums.pop(i)
        else:
            i += 1

    return i
