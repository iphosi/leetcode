from typing import List


def removeElement(nums: List[int], val: int) -> int:
    left = 0
    right = len(nums) - 1

    while right >= left:
        if nums[left] == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1

    return left
