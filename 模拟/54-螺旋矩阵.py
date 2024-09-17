from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    delta = 0

    row = col = 0

    while len(result) < num_rows * num_cols:
        result.append(matrix[row][col])

        if row == delta and col < num_cols - 1 - delta:
            col += 1
        elif row < num_rows - 1 - delta and col == num_cols - 1 - delta:
            row += 1
        elif row == num_rows - 1 - delta and col > delta:
            col -= 1
        elif row > delta and col == delta:
            row -= 1

        if row == col == delta:
            row += 1
            col += 1
            delta += 1

    return result
