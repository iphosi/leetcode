from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    result = nums.copy()
    nums.sort()

    index_dict = {nums[0]: 0}

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            index_dict[nums[i]] = i

    return [index_dict[num] for num in result]
