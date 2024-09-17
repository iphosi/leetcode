from typing import List


def lastStoneWeightII(stones: List[int]) -> int:
    sum_stones = sum(stones)
    target = sum_stones // 2

    dp = [[0] * (target + 1) for _ in range(len(stones))]

    for j in range(stones[0], target + 1):
        dp[0][j] = stones[0]

    for i in range(1, len(stones)):
        for j in range(target + 1):
            if j < stones[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - stones[i]] + stones[i]
                )

    return sum_stones - 2 * dp[-1][-1]


def lastStoneWeightII(stones: List[int]) -> int:
    sum_stones = sum(stones)
    target = sum_stones // 2

    dp = [0] * (target + 1)

    for i in range(len(stones)):
        for j in range(target, stones[i] - 1, -1):
            dp[j] = max(
                dp[j],
                dp[j - stones[i]] + stones[i],
            )

    return sum_stones - 2 * dp[-1]
