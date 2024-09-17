from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        try:
            j = nums.index(target - nums[i])
            if i != j:
                return [i, j]
        except:
            continue


def twoSum(nums: List[int], target: int) -> List[int]:
    index_dict = {}

    for i in range(len(nums)):
        if target - nums[i] in index_dict.keys():
            return [i, index_dict[target - nums[i]]]
        index_dict[nums[i]] = i
