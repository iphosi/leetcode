# dp[i][j]: 使得 word1[:i] 与 word2[:j] 相同所需的最小删除操作数
# word1 = "sea"
# word2 = "eat"
# dp = [
#     [0, 1, 2, 3],
#     [1, 2, 3, 4],
#     [2, 1, 2, 3],
#     [3, 2, 1, 2]
# ]


def minDistance(word1: str, word2: str) -> int:
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    for i in range(1, len(word1) + 1):
        dp[i][0] = i

    for j in range(1, len(word2) + 1):
        dp[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[-1][-1]
