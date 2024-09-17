# dp[i][j]: word1[:i] 与 word2[:j] 的最小编辑距离
# word1 = "horse"
# word2 = "ros"
# dp = [
#     [0, 1, 2, 3],
#     [1, 1, 2, 3],
#     [2, 2, 1, 2],
#     [3, 2, 2, 2],
#     [4, 3, 3, 2],
#     [5, 4, 4, 3],
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
                # dp[i - 1][j] + 1: word1 删除一个元素（word2添加一个元素，相当于word1删除一个元素）
                # dp[i][j - 1] + 1: word2 删除一个元素
                # dp[i - 1][j - 1] + 1: 替换元素
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[-1][-1]
