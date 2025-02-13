from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # mid 位于值较大的有序数组中，nums[:mid] 为有序子数组
        if nums[mid] >= nums[0]:
            # target 位于有序子数组中
            if nums[0] <= target < nums[mid]:
                right = mid - 1
            # target 不位于有序子数组中
            else:
                left = mid + 1
        # mid 位于值较小的有序数组中，nums[mid:] 为有序子数组
        else:
            # target 位于有序子数组中
            if nums[mid] < target <= nums[-1]:
                left = mid + 1
            # target 不位于有序子数组中
            else:
                right = mid - 1

    return -1


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
