from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    row = 0

    while row < num_rows and matrix[row][0] <= target:
        row += 1

    row -= 1

    left = 0
    right = num_cols - 1

    while left <= right:
        mid = (left + right) // 2

        if matrix[row][mid] > target:
            right = mid - 1
        elif matrix[row][mid] < target:
            left = mid + 1
        else:
            return True

    return False
