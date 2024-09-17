from typing import List


# 完全背包组合问题


def coinChange(coins: List[int], amount: int) -> int:
    dp = [[0] * (amount + 1) for _ in range(len(coins))]

    for j in range(1, amount + 1):
        if j % coins[0] == 0:
            dp[0][j] = j // coins[0]
        else:
            dp[0][j] = -1

    for i in range(1, len(coins)):
        for j in range(1, amount + 1):
            if j < coins[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                if dp[i - 1][j] == -1 and dp[i][j - coins[i]] == -1:
                    dp[i][j] = -1
                elif dp[i - 1][j] == -1:
                    dp[i][j] = dp[i][j - coins[i]] + 1
                elif dp[i][j - coins[i]] == -1:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - coins[i]] + 1,
                    )

    return dp[-1][-1]


def coinChange(coins: List[int], amount: int) -> int:
    dp = [0] * (amount + 1)

    for j in range(1, amount + 1):
        if j % coins[0] == 0:
            dp[j] = j // coins[0]
        else:
            dp[j] = -1

    for i in range(1, len(coins)):
        for j in range(coins[i], amount + 1):
            if dp[j] == -1 and dp[j - coins[i]] == -1:
                dp[j] = -1
            elif dp[j] == -1:
                dp[j] = dp[j - coins[i]] + 1
            elif dp[j - coins[i]] == -1:
                dp[j] = dp[j]
            else:
                dp[j] = min(
                    dp[j],
                    dp[j - coins[i]] + 1,
                )

    return dp[-1]


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)

    dp[0] = 0

    for j in range(1, amount + 1):
        if j % coins[0] == 0:
            dp[j] = j // coins[0]

    for i in range(1, len(coins)):
        for j in range(coins[i], amount + 1):
            dp[j] = min(
                dp[j],
                dp[j - coins[i]] + 1,
            )

    return dp[-1] if dp[-1] != float("inf") else -1


def coinChange(coins: List[int], amount: int):
    dp = [float("inf") for _ in range(amount + 1)]
    dp[0] = 0

    for coin in coins:
        # 用面值为 coin 的硬币凑成金额 i
        for i in range(coin, amount + 1):
            if dp[i - coin] != float("inf"):
                # 使用旧硬币凑成金额 i 所需的最小硬币数量
                # 凑成金额 i - coin 所需的最小硬币数量加上一枚面值为 coin 的新硬币
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[-1] == float("inf"):
        return -1
    else:
        return dp[-1]
