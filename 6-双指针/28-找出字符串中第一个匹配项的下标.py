

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


def strStr(haystack: str, needle: str) -> int:
    left = 0
    right = len(needle)

    while right <= len(haystack):
        if haystack[left:right] == needle:
            return left
        else:
            left += 1
            right += 1

    return -1
