from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = right = 0
    curr_sum = 0
    curr_len = len(nums) + 1

    while right < len(nums):
        if curr_sum < target:
            curr_sum += nums[right]
            right += 1

            while curr_sum >= target and left < right:
                curr_len = min(curr_len, right - left)
                curr_sum -= nums[left]
                left += 1

    return curr_len if curr_len <= len(nums) else 0
