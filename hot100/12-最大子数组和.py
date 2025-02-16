from typing import List


# dp[i]: 以 nums[i] 结尾的最大子数组和


def maxSubArray(nums: List[int]) -> int:
    max_sum = dp = nums[0]

    for i in range(1, len(nums)):
        dp = max(nums[i], dp + nums[i])
        max_sum = max(max_sum, dp)

    return max_sum
