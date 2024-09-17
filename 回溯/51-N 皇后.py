from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    result = []

    board = [
        ["." for _ in range(n)]
        for _ in range(n)
    ]

    def is_available(row, col):
        # 仅需检测左侧
        for j in range(col):
            if board[row][j] == "Q":
                return False

        i = row
        j = col

        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if board[i][j] == "Q":
                return False

        i = row
        j = col

        while i < n - 1 and j > 0:
            i += 1
            j -= 1
            if board[i][j] == "Q":
                return False

        return True

    def backtrack(curr_col):
        if curr_col == n:
            result.append(["".join(row) for row in board])
            return

        for curr_row in range(n):
            if is_available(curr_row, curr_col):
                board[curr_row][curr_col] = "Q"
                backtrack(curr_col + 1)
                board[curr_row][curr_col] = "."

    backtrack(0)

    return result
