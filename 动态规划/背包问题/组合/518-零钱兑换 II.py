from typing import List


# 完全背包组合问题
# 外层 for 遍历物品，内层 for 循环遍历背包


def change(amount: int, coins: List[int]) -> int:
    dp = [[0] * (amount + 1) for _ in range(len(coins))]

    for i in range(len(coins)):
        dp[i][0] = 1

    for j in range(coins[0], amount + 1, coins[0]):
        dp[0][j] = 1

    for i in range(1, len(coins)):
        for j in range(1, amount + 1):
            if j < coins[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                # dp[i][j - coins[i]]: 用 coins[i] 的情况下，装满 j - coins[i] 的方法数量
                # 由于是完全背包，装满 j - coins[i] 时也可以用 coins[i]
                # dp[i - 1][j]: 不用 coins[i] 的情况下，装满 j 的方法数量
                dp[i][j] = dp[i][j - coins[i]] + dp[i - 1][j]

    return dp[-1][-1]


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)

    dp[0] = 1

    for j in range(coins[0], amount + 1, coins[0]):
        dp[j] = 1

    for i in range(1, len(coins)):
        for j in range(coins[i], amount + 1):
            dp[j] += dp[j - coins[i]]

    return dp[-1]

