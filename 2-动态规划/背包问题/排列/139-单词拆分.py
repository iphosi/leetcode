from typing import List


# dp[i]: s[:i + 1] 是否可以通过拼接得到


def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True

    word_set = set(wordDict)

    for i in range(1, len(s) + 1):
        for j in range(i):
            if not dp[i]:
                dp[i] = dp[j] and s[j:i] in word_set
            else:
                break

    return dp[-1]
