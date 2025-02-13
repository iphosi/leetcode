def func(text1, text2):
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    for i in range(1, len(text1) + 1):
        dp[i][0] = dp[i - 1][0] + ord(text1[i - 1])

    for j in range(1, len(text2) + 1):
        dp[0][j] = dp[0][j - 1] + ord(text2[j - 1])

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + ord(text1[i - 1]),
                    dp[i][j - 1] + ord(text2[j - 1])
                )

    return dp[-1][-1]


s1 = input()
s2 = input()

print(func(s1, s2))
