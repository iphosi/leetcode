# 同 647-回文子串


def longestPalindrome(s: str) -> str:
    start = end = 0
    max_length = 0

    dp = [[False] * len(s) for _ in range(len(s))]

    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j] and (j - i + 1) > max_length:
                max_length = max(max_length, j - i + 1)
                start = i
                end = j + 1

    return s[start:end]
