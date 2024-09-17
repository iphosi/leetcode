from typing import List


def removeElement(nums: List[int], val: int) -> int:
    index = 0

    while index < len(nums):
        if nums[index] == val:
            nums.pop(index)
        else:
            index += 1

    return index


def removeElement(nums: List[int], val: int) -> int:
    left = right = 0

    while right < len(nums):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
        right += 1

    return left


def removeElement(nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1

        return left


def removeElement(nums: List[int], val: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        # 将右指针处的值赋到左指针处
        # 直至左指针处的值不等于需要删除的值
        # 则最终列表的长度可加一
        if nums[left] == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1

    return left
