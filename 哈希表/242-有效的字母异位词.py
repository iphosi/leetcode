from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_dict = defaultdict(int)

    for i in range(len(s)):
        count_dict[s[i]] += 1
        count_dict[t[i]] -= 1

    return all(map(lambda v: v == 0, count_dict.values()))
