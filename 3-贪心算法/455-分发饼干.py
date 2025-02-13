from typing import List


def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    i = j = 0

    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            i += 1
        j += 1

    return i
