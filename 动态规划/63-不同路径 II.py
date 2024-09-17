from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = 1
        else:
            break

    for j in range(n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = 1
        else:
            break

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                continue

    return dp[-1][-1]


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [0] * n

    for j in range(n):
        if obstacleGrid[0][j] == 0:
            dp[j] = 1
        else:
            break

    for i in range(1, m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]

    return dp[-1]
