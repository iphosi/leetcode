from typing import List


# 到达第 i 级台阶，可以从第 i - 1 级或第 i - 2 级台阶出发
# 到达第 i - 1 级台阶所需的最小费用加上从第 i - 1 级台阶前进所需的费用
# 到达第 i - 2 级台阶所需的最小费用加上从第 i - 2 级台阶前进所需的费用
# 两者取最小值，即为到达第 i 级台阶所需的最小费用

def minCostClimbingStairs(cost: List[int]) -> int:
    dp = [0, 0]

    for i in range(2, len(cost) + 1):
        dp = [
            dp[1],
            min(
                dp[0] + cost[i - 2],
                dp[1] + cost[i - 1],
            )
        ]

    return dp[1]
