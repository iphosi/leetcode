from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()

    def backtrack(curr_path, curr_start, curr_used, curr_target):
        if curr_target == 0:
            result.append(curr_path.copy())

        for i in range(curr_start, len(candidates)):
            if curr_target - candidates[i] < 0:
                break
            if i > curr_start and candidates[i] == candidates[i - 1] and not curr_used[i - 1]:
                continue
            curr_used[i] = True
            curr_path.append(candidates[i])
            backtrack(curr_path, i + 1, curr_used, curr_target - candidates[i])
            curr_used[i] = False
            curr_path.pop()

    backtrack([], 0, [False for _ in range(len(candidates))], target)

    return result
