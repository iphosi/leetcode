def lengthOfLongestSubstring(s: str) -> int:
    history = set()

    right = -1
    max_len = 0

    for left in range(len(s)):
        if left != 0:
            history.remove(s[left - 1])
        while right + 1 < len(s) and s[right + 1] not in history:
            history.add(s[right + 1])
            right += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    history = {s[0]}

    right = 1
    max_len = 1

    for left in range(len(s)):
        while right < len(s) and s[right] not in history:
            history.add(s[right])
            right += 1

        max_len = max(max_len, right - left)
        history.remove(s[left])

    return max_len