from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        return

    for i in range(m):
        if nums1[i] > nums2[0]:
            nums1[i], nums2[0] = nums2[0], nums1[i]
            nums2.sort()

    for j in range(n):
        nums1[m + j] = nums2[j]


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    pointer = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[pointer] = nums1[i]
            i -= 1
        else:
            nums1[pointer] = nums2[j]
            j -= 1
        pointer -= 1

    if i < 0:
        nums1[:j + 1] = nums2[:j + 1]
