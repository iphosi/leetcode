from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if nums[i] > target > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if nums[i] + nums[j] > target > 0:
                break
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

    return result
