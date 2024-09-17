from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            next_row_list = []
            next_col_list = []

            curr_row = i
            curr_col = j

            for _ in range(3):
                # 顺时针转 90 度
                next_row = curr_col
                next_col = n - 1 - curr_row

                next_row_list.append(next_row)
                next_col_list.append(next_col)

                curr_row = next_row
                curr_col = next_col

            (
                matrix[i][j],
                matrix[next_row_list[0]][next_col_list[0]],
                matrix[next_row_list[1]][next_col_list[1]],
                matrix[next_row_list[2]][next_col_list[2]],
            ) = (
                matrix[next_row_list[2]][next_col_list[2]],
                matrix[i][j],
                matrix[next_row_list[0]][next_col_list[0]],
                matrix[next_row_list[1]][next_col_list[1]],
            )
