from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    zero_list = []

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 0:
                zero_list.append([i, j])

    for i, j in zero_list:
        for row in range(num_rows):
            matrix[row][j] = 0
        for col in range(num_cols):
            matrix[i][col] = 0
