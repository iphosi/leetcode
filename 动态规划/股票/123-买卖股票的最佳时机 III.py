from typing import List


# 状态 0：无操作
# 状态 1：第一次持有股票
# 状态 2：第一次不持有股票
# 状态 3：第二次持有股票
# 状态 4：第二次不持有股票


def maxProfit(prices: List[int]) -> int:
    dp = [[0] * 5 for _ in range(len(prices))]

    dp[0][1] = - prices[0]
    dp[0][3] = - prices[0]

    for i in range(1, len(prices)):
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
        dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

    return dp[-1][-1]
