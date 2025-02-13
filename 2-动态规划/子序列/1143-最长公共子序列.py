# dp[i][j]: s[:i+1] 与 t[:j+1] 的最长公共子序列长度
# text1 = "abc"
# text2 = "ahbgdc"
# dp = [
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 2, 2, 2, 2],
#     [1, 1, 2, 2, 2, 3]
# ]


def longestCommonSubsequence(text1: str, text2: str) -> int:
    max_length = 0
    dp = [[0] * len(text2) for _ in range(len(text1))]

    for i in range(len(text1)):
        if text1[i] == text2[0]:
            for idx in range(i, len(text1)):
                dp[idx][0] = 1
            max_length = 1
            break

    for j in range(len(text2)):
        if text2[j] == text1[0]:
            for idx in range(j, len(text2)):
                dp[0][idx] = 1
            max_length = 1
            break

    for i in range(1, len(text1)):
        for j in range(1, len(text2)):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            max_length = max(max_length, dp[i][j])

    return max_length
