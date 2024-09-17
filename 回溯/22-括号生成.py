from typing import List


def generateParenthesis(n: int) -> List[str]:
    result = []

    def backtrack(curr_path, num_left, num_right):
        if len(curr_path) == 2 * n:
            result.append("".join(curr_path))
            return

        if num_left < n:
            curr_path.append("(")
            backtrack(curr_path, num_left + 1, num_right)
            curr_path.pop()
        if num_right < num_left:
            curr_path.append(")")
            backtrack(curr_path, num_left, num_right + 1)
            curr_path.pop()

    backtrack([], 0, 0)

    return result
