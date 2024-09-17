from typing import List


def letterCombinations(digits: str) -> List[str]:
    if digits == "":
        return []

    result = []
    char_dict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(curr_path, curr_start):
        if len(curr_path) == len(digits):
            result.append("".join(curr_path))
            return

        for char in char_dict[digits[curr_start]]:
            curr_path.append(char)
            backtrack(curr_path, curr_start + 1)
            curr_path.pop()

    backtrack([], 0)

    return result
