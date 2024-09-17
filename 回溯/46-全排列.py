from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(curr_path, curr_used):
        if len(curr_path) == len(nums):
            result.append(curr_path.copy())

        for i in range(len(nums)):
            if not curr_used[i]:
                curr_used[i] = True
                curr_path.append(nums[i])
                backtrack(curr_path, curr_used)
                curr_used[i] = False
                curr_path.pop()

    backtrack([], [False for _ in range(len(nums))])

    return result
