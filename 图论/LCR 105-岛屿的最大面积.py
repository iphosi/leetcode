from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    max_area = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    def dfs(curr_row, curr_col):
        if curr_row < 0 or \
                curr_row > num_rows - 1 or \
                curr_col < 0 or \
                curr_col > num_cols - 1 or \
                grid[curr_row][curr_col] == 0:
            return 0

        grid[curr_row][curr_col] = 0

        return 1 + dfs(curr_row - 1, curr_col) + \
               dfs(curr_row + 1, curr_col) + \
               dfs(curr_row, curr_col - 1) + \
               dfs(curr_row, curr_col + 1)

    for i in range(num_rows):
        for j in range(num_cols):
            max_area = max(max_area, dfs(i, j))

    return max_area


class Solution:
    def __init__(self):
        self.max_area = 0
        self.curr_area = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(curr_row, curr_col):
            if curr_row < 0 or \
                    curr_row > num_rows - 1 or \
                    curr_col < 0 or \
                    curr_col > num_cols - 1 or \
                    grid[curr_row][curr_col] == 0:
                return 0

            grid[curr_row][curr_col] = 0
            self.curr_area += 1

            dfs(curr_row - 1, curr_col)
            dfs(curr_row + 1, curr_col)
            dfs(curr_row, curr_col - 1)
            dfs(curr_row, curr_col + 1)

        for i in range(num_rows):
            for j in range(num_cols):
                self.curr_area = 0
                dfs(i, j)
                self.max_area = max(self.max_area, self.curr_area)

        return self.max_area
