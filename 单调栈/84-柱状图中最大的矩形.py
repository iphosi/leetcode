from typing import List


# 以当前柱子为顶，寻找前一个更低的柱子和后一个更低的柱子
# 前一个更低的柱子索引位于单调递增栈顶
# 在列表头尾添加零，保证每一个柱子前后都有一个更低的柱子

def largestRectangleArea(heights: List[int]) -> int:
    mono_stack = []

    result = 0
    heights.insert(0, 0)
    heights.append(0)

    for i in range(len(heights)):
        while mono_stack and heights[i] < heights[mono_stack[-1]]:
            j = mono_stack.pop()
            if mono_stack:
                result = max(result, (i - mono_stack[-1] - 1) * heights[j])
        mono_stack.append(i)

    return result
