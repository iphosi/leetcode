from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def rob_func(start, end):
        if start == end:
            return nums[start]

        dp = [nums[start], max(nums[start], nums[start + 1])]

        for i in range(start + 2, end + 1):
            dp = [dp[1], max(dp[1], dp[0] + nums[i])]

        return dp[1]

    return max(
        rob_func(0, len(nums) - 2),
        rob_func(1, len(nums) - 1),
    )
