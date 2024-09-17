from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    result = []

    def backtrack(curr_path, curr_start):
        if len(curr_path) == k:
            result.append(curr_path.copy())

        for i in range(curr_start, n + 1):
            curr_path.append(i)
            backtrack(curr_path, i + 1)
            curr_path.pop()

    backtrack([], 1)

    return result
