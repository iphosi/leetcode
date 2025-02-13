from typing import List


# dp[i][0]: 第 i 天持有股票所得最多现金
# dp[i][1]: 第 i 天不持有股票所得最多现金


def maxProfit(prices: List[int]) -> int:
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = - prices[0]

    for i in range(1, len(prices)):
        # dp[i - 1][0]: 第 i-1 天就已经持有股票
        # - prices[i]: 第 i 天买入股票
        dp[i][0] = max(dp[i - 1][0], - prices[i])
        # dp[i - 1][1]: 第 i-1 天就已经卖出股票
        # prices[i] + dp[i - 1][0]: 第 i 天卖出股票
        dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

    return dp[-1][-1]


def maxProfit(prices: List[int]) -> int:
    dp = [0, 0]
    dp[0] = - prices[0]

    for i in range(1, len(prices)):
        dp[0] = max(dp[0], - prices[i])
        dp[1] = max(dp[1], prices[i] + dp[0])

    return dp[1]

