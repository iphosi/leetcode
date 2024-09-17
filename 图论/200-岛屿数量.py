from typing import List


def numIslands(grid: List[List[str]]) -> int:
    result = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    def dfs(curr_row, curr_col):
        if curr_row < 0 or \
                curr_row > num_rows - 1 or \
                curr_col < 0 or \
                curr_col > num_cols - 1 or \
                grid[curr_row][curr_col] == "0":
            return

        grid[curr_row][curr_col] = "0"
        dfs(curr_row - 1, curr_col)
        dfs(curr_row + 1, curr_col)
        dfs(curr_row, curr_col - 1)
        dfs(curr_row, curr_col + 1)

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == "1":
                result += 1
            else:
                continue
            dfs(i, j)

    return result
