from typing import List


def getRow(rowIndex: int) -> List[int]:
    result = [1]

    for _ in range(rowIndex):
        result = [
            i + j
            for i, j in zip(
                [0] + result,
                result + [0]
            )
        ]

    return result
