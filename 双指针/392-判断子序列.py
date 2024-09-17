def isSubsequence(s: str, t: str) -> bool:
    if s == "":
        return True
    elif t == "":
        return False

    p1 = p2 = 0

    while p1 < len(s) and p2 < len(t):
        if t[p2] == s[p1]:
            p1 += 1
        p2 += 1

    return p1 == len(s)
