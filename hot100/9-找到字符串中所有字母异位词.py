from typing import List
from collections import Counter


def findAnagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []

    result = []

    window_size = len(p)
    p_dict = Counter(p)
    s_dict = {key: 0 for key in p_dict.keys()}

    start = 0
    end = start + window_size - 1

    for i in range(start, end + 1):
        if s[i] not in s_dict:
            continue
        else:
            s_dict[s[i]] += 1

    while end < len(s):
        if s_dict == p_dict:
            result.append(start)

        if s[start] in s_dict:
            s_dict[s[start]] -= 1

        start += 1
        end += 1

        if end < len(s):
            if s[end] in s_dict:
                s_dict[s[end]] += 1

    return result
