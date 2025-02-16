from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    result = []
    intervals.sort(key=lambda i: i[0])

    def is_overlapped(interval_a, interval_b):
        return interval_a[0] <= interval_b[0] <= interval_a[1]

    main_interval = intervals[0]
    cand_pointer = 1

    while cand_pointer < len(intervals):
        if is_overlapped(main_interval, intervals[cand_pointer]):
            main_interval[1] = max(main_interval[1], intervals[cand_pointer][1])
        else:
            result.append(main_interval)
            main_interval = intervals[cand_pointer]
        cand_pointer += 1

    result.append(main_interval)

    return result
