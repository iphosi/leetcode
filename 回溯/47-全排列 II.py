from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def backtrack(curr_path, curr_used):
        if len(curr_path) == len(nums):
            result.append(curr_path.copy())
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not curr_used[i - 1]:
                continue
            if not curr_used[i]:
                curr_path.append(nums[i])
                curr_used[i] = True
                backtrack(curr_path, curr_used)
                curr_path.pop()
                curr_used[i] = False

    backtrack([], [False] * len(nums))

    return result
