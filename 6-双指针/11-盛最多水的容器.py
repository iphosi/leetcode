from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1

    max_area = 0

    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(curr_area, max_area)

        # 如果我们移动数字较大的那个指针，那么前者「两个指针指向的数字中较小值」不会增加，后者「指针之间的距离」会减小，那么这个乘积会减小。
        # 因此，我们移动数字较大的那个指针是不合理的。
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
