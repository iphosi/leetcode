# s = "aabaaf"
# prefix_table = [0, 1, 0, 1, 2, 0]
# prefix_table = [-1, 0, -1, 0, 1, -1]


def get_prefix_table(s):
    prefix_table = [0] * len(s)
    j = -1
    prefix_table[0] = j

    for i in range(1, len(s)):
        while j >= 0 and s[i] != s[j + 1]:
            j = prefix_table[j]  # 前后缀不相同，回退

        if s[i] == s[j + 1]:
            j += 1

        prefix_table[i] = j

    return prefix_table


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    prefix_table = get_prefix_table(needle)

    j = -1

    for i in range(len(haystack)):
        while j >= 0 and haystack[i] != needle[j + 1]:
            j = prefix_table[j]

        if haystack[i] == needle[j + 1]:
            j += 1

        if j == len(needle) - 1:
            return i - len(needle) + 1

    return -1
