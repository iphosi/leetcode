from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]

    result = [[1], [1, 1]]

    for _ in range(2, numRows):
        left = right = 0

        curr_row = []

        while left < len(result[-1]) and right < len(result[-1]):
            if left == right:
                curr_row.append(1)
            else:
                curr_row.append(result[-1][left] + result[-1][right])

            if right == 0:
                right += 1
            elif right == len(result[-1]) - 1:
                left += 1
            else:
                left += 1
                right += 1

        result.append(curr_row)

    return result


def generate(numRows: int) -> List[List[int]]:
    result = [[1]]

    for _ in range(1, numRows):
        result.append(
            [
                a + b
                for a, b in zip(
                    [0] + result[-1], result[-1] + [0]
                )
            ]
        )

    return result
