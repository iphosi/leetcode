from typing import List


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def move_to_end(start, end, target):
        while start <= end:
            if nums[start] == target:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1

        return end

    new_end = move_to_end(0, len(nums) - 1, 2)
    _ = move_to_end(0, new_end, 1)
