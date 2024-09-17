from typing import List


def findLengthOfLCIS(nums: List[int]) -> int:
    left = 0
    right = 1

    max_length = 1

    while right < len(nums):
        if nums[right - 1] < nums[right]:
            right += 1
        else:
            left = right
            right += 1

        max_length = max(max_length, right - left)

    return max_length
