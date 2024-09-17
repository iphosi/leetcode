from typing import List

# 01 背包组合问题

# left - right = target
# left + right = sum_nums
# left = (target + sum_nums) / 2


def findTargetSumWays(nums: List[int], target: int) -> int:
    sum_nums = sum(nums)

    if (sum_nums + target) % 2 == 1 or abs(target) > sum_nums:
        return 0

    capacity = (sum_nums + target) // 2

    dp = [[0] * (capacity + 1) for _ in range(len(nums))]

    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
        dp[i][0] = 2 ** zero_count

    if capacity >= nums[0] != 0:
        dp[0][nums[0]] = 1

    for i in range(1, len(nums)):
        for j in range(1, capacity + 1):
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                # dp[i - 1][j - coins[i]]: 用 coins[i] 的情况下，装满 j - coins[i] 的方法数量
                # 由于是 01 背包，装满 j - coins[i] 时不可以用 coins[i]
                # dp[i - 1][j]: 不用 coins[i] 的情况下，装满 j 的方法数量
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]

    return dp[-1][-1]


def findTargetSumWays(nums: List[int], target: int) -> int:
    sum_nums = sum(nums)

    if (target + sum_nums) % 2 == 1 or abs(target) > sum_nums:
        return 0

    capacity = (target + sum(nums)) // 2

    dp = [[0] * (capacity + 1) for _ in range(len(nums) + 1)]
    dp[0][0] = 1

    for i in range(1, len(nums) + 1):
        for j in range(capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1]:
                dp[i][j] += dp[i - 1][j - nums[i - 1]]

    return dp[-1][-1]


def findTargetSumWays(nums: List[int], target: int) -> int:
    sum_nums = sum(nums)

    if (target + sum_nums) % 2 == 1 or abs(target) > sum_nums:
        return 0

    capacity = (target + sum(nums)) // 2

    dp = [0] * (capacity + 1)
    dp[0] = 1
    if capacity >= nums[0]:
        dp[nums[0]] += 1

    for i in range(1, len(nums)):
        for j in range(capacity, nums[i] - 1, -1):
            dp[j] += dp[j - nums[i]]

    return dp[-1]
