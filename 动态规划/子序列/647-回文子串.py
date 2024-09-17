# dp[i][j]: s[i:j+1] 是否为回文串
# s = "cbabc"
# dp = [
#     [1, 0, 0, 0, 1],
#     [0, 1, 0, 1, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1]
# ]
# s = "cbbc"
# dp = [
#     [1, 0, 0, 1],
#     [0, 1, 1, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1]
# ]


def countSubstrings(s: str) -> int:
    result = 0

    dp = [[False] * len(s) for _ in range(len(s))]

    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j]:
                result += 1

    return result
