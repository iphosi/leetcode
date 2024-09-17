from typing import List


def canPartition(nums: List[int]) -> bool:
    sum_nums = sum(nums)
    max_num = max(nums)
    target = sum_nums // 2

    if sum_nums % 2 == 1 or max_num > target:
        return False

    dp = [[0] * (target + 1) for _ in range(len(nums))]

    for j in range(nums[0], target + 1):
        dp[0][j] = nums[0]

    for i in range(1, len(nums)):
        for j in range(target + 1):
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - nums[i]] + nums[i]
                )

    return dp[-1][-1] == target


def canPartition(nums: List[int]) -> bool:
    sum_nums = sum(nums)
    max_num = max(nums)
    target = sum_nums // 2

    if sum_nums % 2 == 1 or max_num > target:
        return False

    dp = [0] * (target + 1)

    for j in range(nums[0], target + 1):
        dp[j] = nums[0]

    for i in range(1, len(nums)):
        for j in range(target, nums[i] - 1, -1):
            dp[j] = max(
                dp[j],
                dp[j - nums[i]] + nums[i]
            )

    return dp[-1] == target
