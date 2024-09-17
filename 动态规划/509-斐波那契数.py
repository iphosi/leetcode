def fib(n: int) -> int:
    dp = [0, 1]

    for i in range(2, n + 1):
        dp.append(dp[i - 2] + dp[i - 1])

    return dp[n]


def fib(n: int) -> int:
    dp = [0, 1]

    if n < 2:
        return dp[n]

    for _ in range(2, n + 1):
        dp = [dp[1], dp[0] + dp[1]]

    return dp[-1]
