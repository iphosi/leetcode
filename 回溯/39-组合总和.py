from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(curr_path, curr_start, curr_target):
        if curr_target == 0:
            result.append(curr_path.copy())

        for i in range(curr_start, len(candidates)):
            if curr_target - candidates[i] < 0:
                continue
            curr_path.append(candidates[i])
            backtrack(curr_path, i, curr_target - candidates[i])
            curr_path.pop()

    backtrack([], 0, target)

    return result


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()

    def backtrack(curr_path, curr_start, curr_target):
        if curr_target == 0:
            result.append(curr_path.copy())

        for i in range(curr_start, len(candidates)):
            if curr_target - candidates[i] < 0:
                break
            curr_path.append(candidates[i])
            backtrack(curr_path, i, curr_target - candidates[i])
            curr_path.pop()

    backtrack([], 0, target)

    return result
