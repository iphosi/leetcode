from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = 0

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
