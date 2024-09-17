from typing import List


# 状态 0：死细胞
# 状态 1：活细胞
# 状态 2：原先是活细胞，变成死细胞
# 状态 3：原先是死细胞，变成活细胞


def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    num_rows = len(board)
    num_cols = len(board[0])

    def count(row, col):
        moves = [
            [1, 0], [-1, 0],
            [0, 1], [0, -1],
            [1, 1], [1, -1],
            [-1, 1], [-1, -1]
        ]

        count = 0

        for move in moves:
            curr_row = row + move[0]
            curr_col = col + move[1]

            if 0 <= curr_row < num_rows and 0 <= curr_col < num_cols:
                # 考虑上一个时间点的状态
                if board[curr_row][curr_col] == 1 or board[curr_row][curr_col] == 2:
                    count += 1

        return count

    for i in range(num_rows):
        for j in range(num_cols):
            curr_count = count(i, j)

            if board[i][j] == 1:
                if curr_count < 2 or curr_count > 3:
                    board[i][j] = 2
            elif board[i][j] == 0:
                if curr_count == 3:
                    board[i][j] = 3

    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] == 2:
                board[i][j] = 0
            elif board[i][j] == 3:
                board[i][j] = 1