from typing import List


def closedIsland(grid: List[List[int]]) -> int:
    result = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    def dfs(curr_row, curr_col):
        if curr_row < 0 or \
                curr_row > num_rows - 1 or \
                curr_col < 0 or \
                curr_col > num_cols - 1 or \
                grid[curr_row][curr_col] == 1:
            return

        grid[curr_row][curr_col] = 1
        dfs(curr_row - 1, curr_col)
        dfs(curr_row + 1, curr_col)
        dfs(curr_row, curr_col - 1)
        dfs(curr_row, curr_col + 1)

    for i in range(num_rows):
        dfs(i, 0)
        dfs(i, num_cols - 1)

    for j in range(1, num_cols - 1):
        dfs(0, j)
        dfs(num_rows - 1, j)

    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            if grid[i][j] == 0:
                result += 1
            else:
                continue
            dfs(i, j)

    return result
