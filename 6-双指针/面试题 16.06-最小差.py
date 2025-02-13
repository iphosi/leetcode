from typing import List


def smallestDifference(a: List[int], b: List[int]) -> int:
    a.sort()
    b.sort()

    result = float("inf")

    i = j = 0

    while i < len(a) and j < len(b):
        result = min(result, abs(a[i] - b[j]))

        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    return result
