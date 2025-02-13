m, capacity = list(map(lambda s: int(s), input().split()))
weights = list(map(lambda s: int(s), input().split()))
values = list(map(lambda s: int(s), input().split()))

dp = [[0] * (capacity + 1) for _ in range(m)]

for j in range(weights[0], capacity + 1):
    dp[0][j] = values[0]

for i in range(1, m):
    for j in range(1, capacity + 1):
        if j >= weights[i]:
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i - 1][j - weights[i]] + values[i]
            )
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])