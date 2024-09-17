from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]

    result = []

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target - 0.5:
            right = mid - 1
        else:
            left = mid + 1

    result.append(left)

    if left > len(nums) - 1:
        return [-1, -1]

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target + 0.5:
            right = mid - 1
        else:
            left = mid + 1

    result.append(left - 1)

    return result if nums[result[0]] == target else [-1, -1]


def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]

    result = []

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    result.append(left)

    if left > len(nums) - 1 or nums[left] != target:
        return [-1, -1]

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    result.append(left - 1)

    return result
