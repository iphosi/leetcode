from typing import List


# 前缀和：用于高效地对区间 [l, r] 内的数求和


def pivotIndex(nums: List[int]) -> int:
    # sum(nums[l:r]) = prefix[r] - prefix[l]
    # nums = [1, 7, 3, 6, 5, 6]
    # prefix = [0, 1, 8, 11, 17, 22]
    # suffix = [0, 6, 11, 17, 20, 27]
    # sum(nums[2:4]) = prefix[4] - prefix[2] = 9
    prefix = []
    suffix = []

    length = len(nums)

    left = 0
    right = length - 1

    while left < length:
        if left == 0:
            prefix.append(0)
            suffix.append(0)
        else:
            prefix.append(nums[left - 1] + prefix[-1])
            suffix.append(nums[right + 1] + suffix[-1])

        left += 1
        right -= 1

    for i in range(length):
        if prefix[i] == suffix[length - 1 - i]:
            return i

    return -1


def pivotIndex(nums: List[int]) -> int:
    # sum(nums[l:r]) = prefix[r] - prefix[l - 1]
    # nums = [1, 7, 3, 6, 5, 6]
    # prefix = [1, 8, 11, 17, 22, 28]
    # suffix = [6, 11, 17, 20, 27, 28]
    # sum(nums[2:4]) = prefix[3] - prefix[1] = 9
    prefix = []
    suffix = []

    length = len(nums)

    left = 0
    right = length - 1

    while left < length:
        if left == 0:
            prefix.append(nums[left])
            suffix.append(nums[right])
        else:
            prefix.append(nums[left] + prefix[-1])
            suffix.append(nums[right] + suffix[-1])

        left += 1
        right -= 1

    for i in range(length):
        if prefix[i] == suffix[length - 1 - i]:
            return i

    return -1
