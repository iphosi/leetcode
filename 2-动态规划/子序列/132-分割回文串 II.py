def minCut(self, s: str) -> int:
    dp = [[False] * len(s) for _ in range(len(s))]

    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

    # dp_cut[i]: 将以 s[i] 结尾的字符串分割成回文子串的最少分割次数
    dp_cut = [float("inf")] * len(s)

    for i in range(len(s)):
        if dp[0][i]:
            dp_cut[i] = 0
        else:
            for j in range(i):
                if dp[j + 1][i]:
                    dp_cut[i] = min(dp_cut[i], dp_cut[j] + 1)

    return dp_cut[-1]


minCut("abbab")