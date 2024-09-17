from typing import List


# dp[i]: 以 nums[i] 结尾的最长递增长子序列长度


def lengthOfLIS(nums: List[int]) -> int:
    max_length = 1
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            # 遍历 i 之前，以 nums[j] 结尾的最长子序列长度
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                max_length = max(max_length, dp[i])

    return max_length
