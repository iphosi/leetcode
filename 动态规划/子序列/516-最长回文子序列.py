# dp[i][j]: s[i:j] 最长回文子序列长度
# s = "bbbab"
# dp = [
#     [1, 2, 3, 3, 4],
#     [0, 1, 2, 2, 3],
#     [0, 0, 1, 1, 3],
#     [0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 1]
# ]


def longestPalindromeSubseq(s: str) -> int:
    dp = [[0] * len(s) for _ in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = 1

    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][-1]
