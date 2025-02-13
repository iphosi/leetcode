from typing import List


def largestSumAfterKNegations(nums: List[int], k: int) -> int:
    nums.sort()

    i = 0

    while k > 0 and i < len(nums):
        if nums[i] < 0:
            nums[i] *= -1
            k -= 1
            i += 1
        else:
            break

    nums.sort()

    if k > 0:
        nums[0] *= (-1 ** k)

    return sum(nums)


def largestSumAfterKNegations(nums: List[int], k: int) -> int:
    nums.sort(key=lambda num: abs(num))

    i = len(nums) - 1

    while k > 0 and i > 0:
        if nums[i] < 0:
            nums[i] *= -1
            k -= 1
        i -= 1

    if k > 0:
        nums[0] *= (-1) ** k

    return sum(nums)
