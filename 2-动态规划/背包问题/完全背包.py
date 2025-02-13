# 完全背包
# 有 n 件物品和一个最多能背重量为 w 的背包。第i件物品的重量是 weights[i]，得到的价值是 values[i]。
# 每件物品可以无限使用，求解将哪些物品装入背包里物品价值总和最大。


def func_2d(weights, values, capacity):
    # 二维数组
    dp = [[0] * (capacity + 1) for _ in range(len(weights))]

    # 初始化
    for j in range(weights[0], capacity + 1):
        dp[0][j] = values[0] * j // weights[0]

    for i in range(1, len(weights)):  # 遍历物品
        for j in range(capacity + 1):  # 遍历背包容量
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])

    return dp[len(weights) - 1][capacity]


def func_1d(weights, values, capacity):
    # 一维数组
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):  # 遍历物品
        for j in range(weights[i], capacity + 1):  # 遍历背包容量
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[capacity]
