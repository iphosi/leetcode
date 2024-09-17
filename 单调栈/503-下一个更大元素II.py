from typing import List


def nextGreaterElements(nums: List[int]) -> List[int]:
    mono_stack = []
    result = [-1 for _ in range(len(nums))]

    for i in range(2 * len(nums)):
        while mono_stack and nums[i % len(nums)] > nums[mono_stack[-1]]:
            j = mono_stack.pop()
            result[j] = nums[i % len(nums)]

        mono_stack.append(i % len(nums))

    return result
