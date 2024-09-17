from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    num_rows = len(board)
    num_cols = len(board[0])

    used = [
        [False for _ in range(num_cols)]
        for _ in range(num_rows)
    ]

    def backtrack(curr_used, curr_target_idx, curr_row, curr_col):
        if curr_target_idx == len(word):
            return True
        if curr_row < 0 or curr_row == num_rows or curr_col < 0 or curr_col == num_cols:
            return False
        if curr_used[curr_row][curr_col]:
            return False

        if board[curr_row][curr_col] == word[curr_target_idx]:
            curr_used[curr_row][curr_col] = True
            flag_0 = backtrack(curr_used, curr_target_idx + 1, curr_row - 1, curr_col)
            flag_1 = backtrack(curr_used, curr_target_idx + 1, curr_row + 1, curr_col)
            flag_2 = backtrack(curr_used, curr_target_idx + 1, curr_row, curr_col - 1)
            flag_3 = backtrack(curr_used, curr_target_idx + 1, curr_row, curr_col + 1)
            curr_used[curr_row][curr_col] = False
            return flag_0 or flag_1 or flag_2 or flag_3
        else:
            return False

    for i in range(num_rows):
        for j in range(num_cols):
            if backtrack(used, 0, i, j):
                return True

    return False
