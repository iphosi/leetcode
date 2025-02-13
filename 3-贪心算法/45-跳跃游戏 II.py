from typing import List


def jump(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    num_steps = 0
    start = 0
    horizon = 1 + nums[0]

    while horizon < len(nums):
        for i in range(start + 1, horizon):
            if i + nums[i] + 1 > horizon:
                start = i
                horizon = i + nums[i] + 1

        num_steps += 1

    return num_steps + 1
