from typing import List


# dp_large[i]: 将 nums[i] 作为极大值时，最长的摆动序列长度
# dp_small[i]: 将 nums[i] 作为极小值时，最长的摆动序列长度
# nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
# dp_large = [1, 2, 2, 4, 4, 4, 4, 2, 6, 6]
# dp_small = [1, 1, 3, 3, 3, 3, 5, 5, 3, 7]


def wiggleMaxLength(nums: List[int]) -> int:
    result = 1
    dp_large = [1] * len(nums)
    dp_small = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp_large[i] = max(dp_large[i], dp_small[j] + 1)
                result = max(result, dp_large[i])
            elif nums[i] < nums[j]:
                dp_small[i] = max(dp_small[i], dp_large[j] + 1)
                result = max(result, dp_small[i])
            else:
                dp_large[i] = max(dp_large[i], dp_large[j])
                dp_small[i] = max(dp_small[i], dp_small[j])
                result = max(result, dp_large[i], dp_small[i])

    return result
