from typing import  List


def canJump(nums: List[int]) -> bool:
    start = 0
    horizon = 1 + nums[0]
    prev_horizon = 0

    while horizon != prev_horizon:
        if horizon >= len(nums):
            return True
        prev_horizon = horizon
        for i in range(start, horizon):
            if i + nums[i] + 1 > horizon:
                start = i
                horizon = i + nums[i] + 1

    return False