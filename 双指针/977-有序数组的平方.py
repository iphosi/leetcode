from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1

    result = []

    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            result.append(nums[right] ** 2)
            right -= 1
        else:
            result.append(nums[left] ** 2)
            left += 1

    return result[::-1]


def sortedSquares(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
    index = len(nums) - 1

    result = [0] * len(nums)

    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            result[index] = nums[right] ** 2
            right -= 1
        else:
            result[index] = nums[left] ** 2
            left += 1
        index -= 1

    return result
