def func(nums):
    result = 0
    length = len(nums)

    if len(set(nums)) != 1:
        if length % 2 == 1:
            median = nums[length // 2]

            for num in nums:
                if num != median:
                    result += abs(num - median)

        else:
            median_1 = nums[length // 2]
            median_2 = nums[length // 2 - 1]

            result_1 = 0
            result_2 = 0

            for num in nums:
                if num != median_1:
                    result_1 += abs(num - median_1)
                if num != median_2:
                    result_2 += abs(num - median_2)

            result = min(result_1, result_2)

    return result


list_size = int(input())
num_list = [int(char) for char in input().split()]
num_list.sort()

if list_size == 2:
    print(1)
else:
    print(min(func(num_list[1:]), func(num_list[:-1])))
