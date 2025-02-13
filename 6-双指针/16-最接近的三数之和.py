from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    result = None
    nums.sort()

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if result is None or abs(result - target) > abs(curr_sum - target):
                result = curr_sum

            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                break

        if result == 0:
            break

    return result
