from typing import List


# dp_max[i]: 以 nums[i] 结尾的子数组的最大乘积
# dp_min[i]: 以 nums[i] 结尾的子数组的最小乘积
# nums = [2, 3, -2, 4]
# dp_max = [2, 6, -2, 4]
# dp_min = [2, 2, -12, -48]


def maxProduct(nums: List[int]) -> int:
    result = dp_max = dp_min = nums[0]

    for i in range(1, len(nums)):
        prev_dp_max = dp_max
        prev_dp_min = dp_min
        dp_max = max(nums[i], prev_dp_max * nums[i], prev_dp_min * nums[i])
        dp_min = min(nums[i], prev_dp_max * nums[i], prev_dp_min * nums[i])

        result = max(result, dp_max)

    return result
