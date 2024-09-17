from typing import List
from collections import defaultdict


def shortestSeq(big: List[int], small: List[int]) -> List[int]:
    count_dict = defaultdict(int)
    small = set(small)

    left = right = 0

    while right < len(big) and len(count_dict) < len(small):
        if big[right] in small:
            count_dict[big[right]] += 1
        right += 1

    if right == len(big) and len(count_dict) < len(small):
        return []

    min_len = right
    result = [left, right - 1]

    while left < right:
        if big[left] in small:
            count_dict[big[left]] -= 1

            if count_dict[big[left]] == 0:
                if right - left < min_len:
                    min_len = right - left
                    result = [left, right - 1]

                while right < len(big) and count_dict[big[left]] == 0:
                    if big[right] in small:
                        count_dict[big[right]] += 1
                    right += 1

            if count_dict[big[left]] == 0:
                break

        left += 1

    return result
