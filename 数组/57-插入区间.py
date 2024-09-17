from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(intervals) == 0:
        return [newInterval]
    if newInterval[0] > intervals[-1][1]:
        return intervals + [newInterval]

    result = []

    def is_overlapped(interval_1, interval_2):
        return not (interval_1[1] < interval_2[0] or interval_1[0] > interval_2[1])

    i = 0

    while i < len(intervals):
        curr_interval = intervals[i]

        if is_overlapped(curr_interval, newInterval):
            newInterval = [
                min(curr_interval[0], newInterval[0]),
                max(curr_interval[1], newInterval[1])
            ]
            if i == len(intervals) - 1:
                result.append(newInterval)
        elif curr_interval[1] < newInterval[0]:
            result.append(curr_interval)
        else:
            result.append(newInterval)
            break

        i += 1

    result.extend(intervals[i:])

    return result
