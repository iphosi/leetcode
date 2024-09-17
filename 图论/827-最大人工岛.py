from typing import List


class Solution:
    def __init__(self):
        self.curr_key = 2
        self.curr_area = 0
        self.area_dict = {2: 0}

    def largestIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(curr_row, curr_col):
            if curr_row < 0 or curr_row == num_rows or \
                    curr_col < 0 or curr_col == num_cols or \
                    grid[curr_row][curr_col] == 0 or \
                    grid[curr_row][curr_col] != 1:
                return

            grid[curr_row][curr_col] = self.curr_key
            self.curr_area += 1

            dfs(curr_row - 1, curr_col)
            dfs(curr_row + 1, curr_col)
            dfs(curr_row, curr_col - 1)
            dfs(curr_row, curr_col + 1)

        for i in range(num_rows):
            for j in range(num_cols):
                dfs(i, j)
                if self.curr_area != 0:
                    self.area_dict[self.curr_key] = self.curr_area
                    self.curr_key += 1
                    self.curr_area = 0

        max_area = max(self.area_dict.values())

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0:
                    key_set = set()

                    if i > 0 and grid[i - 1][j] >= 2:
                        key_set.add(grid[i - 1][j])
                    if i < num_rows - 1 and grid[i + 1][j] >= 2:
                        key_set.add(grid[i + 1][j])
                    if j > 0 and grid[i][j - 1] >= 2:
                        key_set.add(grid[i][j - 1])
                    if j < num_cols - 1 and grid[i][j + 1] >= 2:
                        key_set.add(grid[i][j + 1])

                    max_area = max(
                        max_area,
                        1 + sum(self.area_dict[key] for key in key_set)
                    )

        return max_area
