# 到达第 i 级台阶，可以从第 i - 1 级或第 i - 2 级台阶出发
# 到达第 i 级台阶的方法数量等于到达第 i - 1 级台阶与到达第 i - 2 级台阶的方法数量之和


def climbStairs(n: int) -> int:
    dp = [1, 2]

    if n < 3:
        return dp[n - 1]

    for _ in range(3, n + 1):
        dp = [dp[1], dp[0] + dp[1]]

    return dp[-1]
