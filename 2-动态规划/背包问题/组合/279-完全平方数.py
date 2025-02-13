def numSquares(n: int):
    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    for num in range(1, int(n ** 0.5) + 1):
        for i in range(num ** 2, n + 1):
            dp[i] = min(dp[i], dp[i - num ** 2] + 1)

    return dp[-1]
