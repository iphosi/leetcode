from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    row = col = delta = 0
    val = 1

    result = [[0 for _ in range(n)] for _ in range(n)]

    while val <= n ** 2:
        result[row][col] = val
        val += 1

        if row == delta and col < n - delta - 1:
            col += 1
        elif row < n - delta - 1 and col == n - delta - 1:
            row += 1
        elif row == n - delta - 1 and col > delta:
            col -= 1
        elif row > delta and col == delta:
            row -= 1

        if row == col == delta:
            delta += 1
            row = col = delta

    return result
