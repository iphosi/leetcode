from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(curr_path, curr_start):
        result.append(curr_path.copy())

        if curr_start == len(nums):
            return

        for i in range(curr_start, len(nums)):
            curr_path.append(nums[i])
            backtrack(curr_path, i + 1)
            curr_path.pop()

    backtrack([], 0)

    return result
