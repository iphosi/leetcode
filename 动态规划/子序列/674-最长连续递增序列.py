from typing import List


# dp[i]: 以 nums[i] 结尾的最长连续递增序列长度


def findLengthOfLCIS(nums: List[int]) -> int:
    max_length = 1
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
        max_length = max(max_length, dp[i])

    return max_length
