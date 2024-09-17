import random


def get_pivot(nums, start, end):
    # 避免长时间无法交换
    rand_idx = random.randint(start, end)
    nums[start], nums[rand_idx] = nums[rand_idx], nums[start]

    p = start
    j = start + 1

    for i in range(start + 1, end + 1):
        if nums[i] <= nums[p]:
            nums[i], nums[j] = nums[j], nums[i]  # 将比 nums[p] 小的元素交换到 j 左侧
            j += 1  # j 指向第一个大于 nums[p] 的元素

    # 与最后一个小于 nums[p] 的元素交换
    # 使得 j - 1 左侧的元素均小于 nums[j - 1]，右侧的值均大于 nums[j - 1]
    nums[p], nums[j - 1] = nums[j - 1], nums[p]

    return j - 1


def quick_sort(nums, start, end):
    if start >= end:
        return

    pivot = get_pivot(nums, start, end)
    quick_sort(nums, start, pivot - 1)
    quick_sort(nums, pivot + 1, end)


num_list = [2, 3, 4, 0, 9, 8, 7, 6]
quick_sort(num_list, 0, len(num_list) - 1)

pass
