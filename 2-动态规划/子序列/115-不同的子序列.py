# dp[i][j]: s[:i+1] 含有 t[:j+1] 的个数
# s = "rabbbit"
# t = "rabbit"
# dp = [
#     [1, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0],
#     [1, 1, 2, 1, 0, 0],
#     [1, 1, 3, 3, 0, 0],
#     [1, 1, 3, 3, 3, 0],
#     [1, 1, 3, 3, 3, 3]
# ]


def numDistinct(s: str, t: str) -> int:
    dp = [[0] * len(t) for _ in range(len(s))]

    for i in range(len(s)):
        if s[i] == t[0]:
            if i == 0:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0] + 1
        else:
            dp[i][0] = dp[i - 1][0]

    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]
