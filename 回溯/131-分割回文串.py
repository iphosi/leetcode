from typing import List


def partition(s: str) -> List[List[str]]:
    result = []

    def is_palindromic(text):
        return text == text[::-1]

    def backtrack(curr_path, curr_start):
        if curr_start == len(s):
            result.append(curr_path.copy())
            return

        for curr_end in range(curr_start + 1, len(s) + 1):
            if is_palindromic(s[curr_start:curr_end]):
                curr_path.append(s[curr_start:curr_end])
                backtrack(curr_path, curr_end)
                curr_path.pop()
            else:
                continue

    backtrack([], 0)

    return result
