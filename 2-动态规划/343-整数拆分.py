def integerBreak(n: int) -> int:
    dp = [1] * (n + 1)

    for i in range(3, n + 1):
        for j in range(2, i):
            dp[i] = max(
                dp[i],
                dp[i - j] * j,
                (i - j) * j
            )

    return dp[-1]
