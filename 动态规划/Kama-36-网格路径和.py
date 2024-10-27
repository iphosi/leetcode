nums = eval(input())

m = len(nums)
n = len(nums[0])

dp = [[0] * n for _ in range(m)]
dp[0][0] = nums[0][0]

for i in range(1, m):
    dp[i][0] = dp[i - 1][0] + nums[i][0]

for j in range(1, n):
    dp[0][j] = dp[0][j - 1] + nums[0][j]

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + nums[i][j]

print(dp[-1][-1])