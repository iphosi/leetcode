from typing import List


# 到达第 i - 2 间房时的最大收益加上偷第 i 间房的收益
# 到达第 i - 1 间房时的最大收益
# 两者取最大值，即为到达第 i 间房时的最大收益

def rob(nums: List[int]) -> int:
    if len(nums) < 2:
        return nums[0]

    dp = [nums[0], max(nums[0], nums[1])]

    for i in range(2, len(nums)):
        dp = [
            dp[1],
            max(
                dp[0] + nums[i],
                dp[1],
            )
        ]

    return dp[1]
