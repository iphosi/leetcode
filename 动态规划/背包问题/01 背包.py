# 01 背包
# 有 n 件物品和一个最多能背重量为 w 的背包。第i件物品的重量是 weights[i]，得到的价值是 values[i]。
# 每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
# dp[i][j]：从下标为 [0-i] 的物品里任意取，放进容量为 j 的背包，价值总和最大是多少。
# 不放物品 i：
# 由 dp[i - 1][j] 推出，即背包容量为 j，里面不放物品 i 的最大价值，此时 dp[i][j] 就是 dp[i - 1][j]。
# 当物品i的重量大于背包 j 的重量时，物品 i 无法放进背包中，所以背包内的价值依然和前面相同。
# 放物品 i：
# 由 dp[i - 1][j - weights[i]] 推出。
# dp[i - 1][j - weights[i]] 为背包容量为 j - weights[i] 的时候不放物品 i 的最大价值。
# dp[i - 1][j - weights[i]] + values[i] 是背包放物品 i 得到的最大价值。
# dp[i][0]: 如果背包容量 j 为 0，无论是选取哪些物品，背包价值总和一定为 0。
# dp[0][j]: 存放编号 0 的物品的时候，各个容量的背包所能存放的最大价值。
# 若 j < weights[0]，背包容量比编号 0 的物品重量还小，最大价值为 0。
# 若 j >= weights[0]，背包容量放足够放编号 0 的物品，最大价值是 value[0]。


def func_2d(weights, values, capacity):
    # 二维数组
    dp = [[0] * (capacity + 1) for _ in range(len(weights))]

    # 初始化
    for j in range(weights[0], capacity + 1):
        dp[0][j] = values[0]

    # weight数组的大小就是物品个数
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
        for j in range(capacity, weights[i] - 1, -1):  # 遍历背包容量
            # 倒序遍历，因为 dp[i][j + k] 不影响 dp[i][j]
            # 若正序遍历，dp[i][j - k] 会覆盖 dp[i - 1][j - k]，相当于一件物品被重复放入
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[capacity]
