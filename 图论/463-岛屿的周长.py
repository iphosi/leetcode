from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    result = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                if i == 0:
                    result += 1
                else:
                    result += grid[i - 1][j] == 0
                if i == num_rows - 1:
                    result += 1
                else:
                    result += grid[i + 1][j] == 0
                if j == 0:
                    result += 1
                else:
                    result += grid[i][j - 1] == 0
                if j == num_cols - 1:
                    result += 1
                else:
                    result += grid[i][j + 1] == 0

    return result
