from typing import List


# dp[i][0]: 第 i 天持有股票所得最多现金
# dp[i][1]: 第 i 天不持有股票所得最多现金


def maxProfit(prices: List[int]) -> int:
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = - prices[0]

    for i in range(1, len(prices)):
        # dp[i - 1][1] - prices[i]: 加上第 i 天前获得的利润
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1],  dp[i - 1][0] + prices[i])

    return dp[-1][-1]


def maxProfit(prices: List[int]) -> int:
    dp = [0, 0]
    dp[0] = - prices[0]

    for i in range(1, len(prices)):
        dp[0] = max(dp[0], dp[1] - prices[i])
        dp[1] = max(dp[1], dp[0] + prices[i])

    return dp[1]