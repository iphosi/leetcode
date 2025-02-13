from typing import List


# dp[i][0]: 以 nums[i] 结尾的最长递增长子序列长度
# dp[i][1]: 以 nums[i] 结尾的最长递增长子序列个数


def findNumberOfLIS(nums: List[int]) -> int:
    max_len = 1
    result = 0

    dp = [[1, 1] for _ in range(len(nums))]

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i][0] < dp[j][0] + 1:
                    # 找到了一个更长的递增子序列
                    dp[i][0] = dp[j][0] + 1
                    dp[i][1] = dp[j][1]
                elif dp[i][0] == dp[j][0] + 1:
                    # 找到了两个相同长度的递增子序列
                    dp[i][1] += dp[j][1]

            max_len = max(max_len, dp[i][0])

    for i in range(len(nums)):
        if dp[i][0] == max_len:
            result += dp[i][1]

    return result
