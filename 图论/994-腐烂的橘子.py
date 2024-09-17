from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    time = 0

    num_rows = len(grid)
    num_cols = len(grid[0])

    curr_rot_list = []
    visited = [
        [False for _ in range(num_cols)]
        for _ in range(num_rows)
    ]

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 2:
                visited[i][j] = True
                curr_rot_list.append([i, j])
            elif grid[i][j] == 0:
                visited[i][j] = True

    while curr_rot_list:
        next_rot_list = []

        for rot in curr_rot_list:
            curr_row = rot[0]
            curr_col = rot[1]

            if curr_row > 0:
                if not visited[curr_row - 1][curr_col] and grid[curr_row - 1][curr_col] == 1:
                    visited[curr_row - 1][curr_col] = True
                    grid[curr_row - 1][curr_col] = 2
                    next_rot_list.append([curr_row - 1, curr_col])
            if curr_row < num_rows - 1:
                if not visited[curr_row + 1][curr_col] and grid[curr_row + 1][curr_col] == 1:
                    visited[curr_row + 1][curr_col] = True
                    grid[curr_row + 1][curr_col] = 2
                    next_rot_list.append([curr_row + 1, curr_col])
            if curr_col > 0:
                if not visited[curr_row][curr_col - 1] and grid[curr_row][curr_col - 1] == 1:
                    visited[curr_row][curr_col - 1] = True
                    grid[curr_row][curr_col - 1] = 2
                    next_rot_list.append([curr_row, curr_col - 1])
            if curr_col < num_cols - 1:
                if not visited[curr_row][curr_col + 1] and grid[curr_row][curr_col + 1] == 1:
                    visited[curr_row][curr_col + 1] = True
                    grid[curr_row][curr_col + 1] = 2
                    next_rot_list.append([curr_row, curr_col + 1])

        if next_rot_list:
            time += 1

        curr_rot_list = next_rot_list

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                return -1

    return time
