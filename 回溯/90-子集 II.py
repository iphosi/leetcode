from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def backtrack(curr_path, curr_start, curr_used):
        result.append(curr_path.copy())

        for i in range(curr_start, len(nums)):
            if i > curr_start and nums[i] == nums[i - 1] and not curr_used[i - 1]:
                continue
            curr_used[i] = True
            curr_path.append(nums[i])
            backtrack(curr_path, i + 1, curr_used)
            curr_used[i] = False
            curr_path.pop()

    backtrack([], 0, [False] * len(nums))

    return result
