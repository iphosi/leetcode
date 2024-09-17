from typing import List


def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= nums[0]:
            left = mid + 1
        else:
            right = mid - 1

    return nums[left] if left < len(nums) else nums[0]


def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left]
