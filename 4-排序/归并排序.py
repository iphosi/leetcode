def merge(nums, start, mid, end):
    temp = []
    left_start = start
    right_start = mid + 1

    while left_start <= mid and right_start <= end:
        if nums[left_start] < nums[right_start]:
            temp.append(nums[left_start])
            left_start += 1
        else:
            temp.append(nums[right_start])
            right_start += 1

    temp.extend(nums[left_start:mid + 1])
    temp.extend((nums[right_start:end + 1]))

    for i in range(start, end + 1):
        nums[i] = temp[i - start]


def merge_sort(nums, start, end):
    if start == end:
        return

    mid = (start + end) // 2

    merge_sort(nums, start, mid)
    merge_sort(nums, mid + 1, end)
    merge(nums, start, mid, end)


num_list = [2, 3, 4, 0, 9, 8, 7, 6]
merge_sort(num_list, 0, len(num_list) - 1)

pass
