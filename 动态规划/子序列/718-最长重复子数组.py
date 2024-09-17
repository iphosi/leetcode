from typing import List


# dp[i][j]: 以 nums1[i] 结尾的数组与以 nums2[j] 结尾的数组的最长重复子数组长度
# nums1 = [1,2,3,2,1]
# nums2 = [3,2,1,4,7]
# dp = [
#     [0, 0, 1, 0, 0],
#     [0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 0],
#     [0, 2, 0, 0, 0],
#     [0, 0, 3, 0, 0]
# ]


def findLength(nums1: List[int], nums2: List[int]) -> int:
    max_length = 0
    dp = [[0] * len(nums2) for _ in range(len(nums1))]

    for i in range(len(nums1)):
        if nums1[i] == nums2[0]:
            dp[i][0] = 1
            max_length = 1

    for j in range(len(nums2)):
        if nums2[j] == nums1[0]:
            dp[0][j] = 1
            max_length = 1

    for i in range(1, len(nums1)):
        for j in range(1, len(nums2)):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            max_length = max(max_length, dp[i][j])

    return max_length


findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7])


def findLength(nums1: List[int], nums2: List[int]) -> int:
    max_length = 0
    dp = [0] * len(nums2)

    for j in range(len(nums2)):
        if nums2[j] == nums1[0]:
            dp[j] = 1
            max_length = 1

    for i in range(1, len(nums1)):
        for j in range(len(nums2) - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[j] = dp[j - 1] + 1 if j > 0 else 1
            else:
                dp[j] = 0
            max_length = max(max_length, dp[j])

    return max_length



