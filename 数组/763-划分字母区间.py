from typing import List


def partitionLabels(s: str) -> List[int]:
    result = []

    def is_overlapped(slice_a, slice_b):
        return slice_a[0] <= slice_b[0] <= slice_a[1]

    char_history = set()
    slice_list = []

    for char in s:
        if char not in char_history:
            char_history.add(char)
            slice_list.append([s.find(char), s.rfind(char)])
        else:
            continue

    main_slice = slice_list[0]
    cand_pointer = 1

    while cand_pointer < len(slice_list):
        if is_overlapped(main_slice, slice_list[cand_pointer]):
            main_slice[1] = max(main_slice[1], slice_list[cand_pointer][1])
        else:
            result.append(main_slice[1] - main_slice[0] + 1)
            main_slice = slice_list[cand_pointer]
        cand_pointer += 1

    result.append(main_slice[1] - main_slice[0] + 1)

    return result
