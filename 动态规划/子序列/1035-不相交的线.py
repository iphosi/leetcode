from typing import List


# 同 1143-最长公共子序列


def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    count = 0
    dp = [[0] * len(nums2) for _ in range(len(nums1))]

    for i in range(len(nums1)):
        if nums1[i] == nums2[0]:
            for idx in range(i, len(nums1)):
                dp[idx][0] = 1
            count = 1
            break

    for j in range(len(nums2)):
        if nums2[j] == nums1[0]:
            for idx in range(j, len(nums2)):
                dp[0][idx] = 1
            count = 1
            break

    for i in range(1, len(nums1)):
        for j in range(1, len(nums2)):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            count = max(count, dp[i][j])

    return count
