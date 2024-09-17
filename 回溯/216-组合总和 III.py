from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    result = []

    def backtrack(curr_path, curr_target, curr_start):
        if len(curr_path) == k:
            if curr_target == 0:
                result.append(curr_path.copy())
            return

        for i in range(curr_start, 10):
            if curr_target - i < 0:
                break
            curr_path.append(i)
            backtrack(curr_path, curr_target - i, i + 1)
            curr_path.pop()

    backtrack([], n, 1)

    return result
