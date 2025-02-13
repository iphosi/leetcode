from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = right = len(nums) - 1

    # 寻找较小数，较小数之后的元素单调递减
    while left > 0 and nums[left - 1] >= nums[left]:
        left -= 1

    # 若 left = 0，说明当前数组的字典序已是最大值
    if left > 0:
        # 在单调递减区间内，从右向左找第一个大于较小数的元素，并交换两者的值
        # 交换值后不改变单调性
        while right > 0 and nums[left - 1] >= nums[right]:
            right -= 1

        nums[left - 1], nums[right] = nums[right], nums[left - 1]

    # 将单调递减区间转化为单调递增区间，使得字典序的变化幅度最小
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
