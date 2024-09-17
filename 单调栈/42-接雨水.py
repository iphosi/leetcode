from typing import List


# 以当前柱子为底，寻找前一个更高的柱子和后一个更高的柱子
# 前一个更高的柱子索引位于单调递减栈顶
# 若栈为空则说明没有前一个更高的柱子

def trap(height: List[int]) -> int:
    mono_stack = []

    result = 0

    for i in range(len(height)):
        while mono_stack and height[i] > height[mono_stack[-1]]:
            bottom_idx = mono_stack.pop()
            if mono_stack:
                left_idx = mono_stack[-1]
                right_idx = i
                result += (right_idx - left_idx - 1) * \
                          (min(height[left_idx], height[right_idx]) - height[bottom_idx])

        mono_stack.append(i)

    return result

