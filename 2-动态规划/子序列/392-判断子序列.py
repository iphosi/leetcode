# dp[i][j]: s[:i+1] 与 t[:j+1] 的最长公共子序列长度
# s = "abc"
# t = "ahbgdc"
# dp = [
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 2, 2, 2, 2],
#     [1, 1, 2, 2, 2, 3]
# ]


def isSubsequence(s: str, t: str) -> bool:
    if s == "":
        return True
    elif t == "":
        return False

    max_length = 0
    dp = [[0] * len(t) for _ in range(len(s))]

    for i in range(len(s)):
        if s[i] == t[0]:
            for idx in range(i, len(s)):
                dp[idx][0] = 1
            max_length = 1
            break

    for j in range(len(t)):
        if t[j] == s[0]:
            for idx in range(j, len(t)):
                dp[0][idx] = 1
            max_length = 1
            break

    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            max_length = max(max_length, dp[i][j])

    return max_length == len(s)
