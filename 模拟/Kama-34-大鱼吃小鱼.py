n = int(input())

nums = list(map(lambda s: int(s), input().split()))

def func(idx):
    while idx > 0:
        if nums[idx] < nums[idx - 1]:
            nums.pop(idx)
        idx -= 1

prev_len = len(nums)
func(len(nums) - 1)
curr_len = len(nums)

if prev_len == curr_len:
    print(0)
else:
    count = 1

    while curr_len != prev_len:
        prev_len = curr_len
        func(len(nums) - 1)
        curr_len = len(nums)

        if prev_len != curr_len:
            count += 1

    print(count)