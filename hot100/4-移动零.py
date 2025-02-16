from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 快指针找到不为 0 的元素后进行值交换
    slow = fast = 0

    while fast < len(nums):
        while nums[fast] == 0:
            fast += 1
            if fast == len(nums):
                break

        if fast == len(nums):
            break
        nums[slow] = nums[fast]

        slow += 1
        fast += 1

    for i in range(slow, fast):
        nums[i] = 0
