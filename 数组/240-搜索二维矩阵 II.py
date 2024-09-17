from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    curr_row = 0
    curr_col = num_cols - 1

    while 0 <= curr_row < num_rows and 0 <= curr_col < num_cols:
        if matrix[curr_row][curr_col] > target:
            curr_col -= 1
        elif matrix[curr_row][curr_col] < target:
            curr_row += 1
        else:
            return True

    return False
