from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)

    prefix = []
    suffix = []

    left = 0
    right = length - 1

    while left < length:
        if left == 0:
            prefix.append(1)
            suffix.append(1)
        else:
            prefix.append(nums[left - 1] * prefix[-1])
            suffix.append(nums[right + 1] * suffix[-1])
        left += 1
        right -= 1

    return [prefix[i] * suffix[length - 1 - i] for i in range(length)]
