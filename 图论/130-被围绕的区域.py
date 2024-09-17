from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    num_rows = len(board)
    num_cols = len(board[0])

    def dfs(curr_row, curr_col, val):
        if curr_row < 0 or \
                curr_row > num_rows - 1 or \
                curr_col < 0 or \
                curr_col > num_cols - 1 or \
                board[curr_row][curr_col] == "X" or \
                board[curr_row][curr_col] == val:
            return

        board[curr_row][curr_col] = val

        dfs(curr_row - 1, curr_col, val)
        dfs(curr_row + 1, curr_col, val)
        dfs(curr_row, curr_col - 1, val)
        dfs(curr_row, curr_col + 1, val)

    for i in range(num_rows):
        dfs(i, 0, "o")
        dfs(i, num_cols - 1, "o")

    for j in range(1, num_cols - 1):
        dfs(0, j, "o")
        dfs(num_rows - 1, j, "o")

    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "o":
                board[i][j] = "O"
