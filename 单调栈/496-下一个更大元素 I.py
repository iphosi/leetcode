from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    mono_stack = []
    result = [-1 for _ in range(len(nums1))]

    for i in range(len(nums2)):
        while mono_stack and nums2[i] > nums2[mono_stack[-1]]:
            j = mono_stack.pop()

            if nums2[j] in nums1:
                result[nums1.index(nums2[j])] = nums2[i]

        mono_stack.append(i)

    return result


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    mono_stack = []
    result = [-1] * len(nums1)

    num_dict = {}

    for i in range(len(nums2)):
        while mono_stack and nums2[i] > nums2[mono_stack[-1]]:
            j = mono_stack.pop()
            num_dict[nums2[j]] = nums2[i]

        mono_stack.append(i)

    for i in range(len(nums1)):
        if nums1[i] in num_dict:
            result[i] = num_dict[nums1[i]]

    return result