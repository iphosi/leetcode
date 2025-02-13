from typing import List


# 完全背包排列问题
# 外层 for 遍历背包，内层 for 循环遍历物品
# nums = [1, 2, 5]
# target = 5
# dp = [
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 2, 3, 5, 8],
#     [1, 1, 2, 3, 5, 9],
# ]
# dp[2][5] = dp[2][5 - 1] + dp[2][5 - 2] + dp[2][5 - 5] = 5 + 3 + 1
# dp[2][4]: [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
#           => [[1, 1, 1, 1, 1], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1], [2, 2, 1]]
# dp[2][3]: [[1, 1, 1], [1, 2], [2, 1]]
#           => [[1, 1, 1, 2], [1, 2, 2], [2, 1, 2]]
# dp[2][0]: []
#           => [[5]]


def combinationSum4(nums: List[int], target: int) -> int:
    dp = [[0] * (target + 1) for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = 1

    for j in range(nums[0], target + 1, nums[0]):
        dp[0][j] = 1

    for j in range(1, target + 1):
        for i in range(1, len(nums)):
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = sum(
                    dp[i][j - nums[idx]]
                    for idx in range(i + 1)
                    if j >= nums[idx]
                )

    return dp[-1][-1]


def combinationSum4(nums: List[int], target: int) -> int:
    dp = [[0] * (target + 1) for _ in range(len(nums))]

    nums.sort()

    for i in range(len(nums)):
        dp[i][0] = 1

    for j in range(nums[0], target + 1, nums[0]):
        dp[0][j] = 1

    for j in range(1, target + 1):
        for i in range(1, len(nums)):
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = sum(
                    dp[i][j - nums[idx]]
                    for idx in range(i + 1)
                )

    return dp[-1][-1]


def combinationSum4(nums: List[int], target: int) -> int:
    dp = [[0] * (target + 1) for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = 1

    for j in range(1, target + 1):
        for i in range(len(nums)):
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[-1][j - nums[i]]

    return dp[-1][-1]


def combinationSum4(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for j in range(1, target + 1):
        for i in range(len(nums)):
            if j - nums[i] >= 0:
                dp[j] += dp[j - nums[i]]

    return dp[-1]
