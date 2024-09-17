from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    mono_stack = []
    result = [0 for _ in range(len(temperatures))]

    for i in range(len(temperatures)):
        while mono_stack and temperatures[i] > temperatures[mono_stack[-1]]:
            j = mono_stack.pop()
            result[j] = i - j

        mono_stack.append(i)
