def func(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
        max_sum = max(max_sum, dp[i])

    return max_sum


t = int(input())

for _ in range(t):
    n, x = list(map(lambda s: int(s), input().split()))
    a = list(map(lambda s: int(s), input().split()))

    result = func(a)

    for i in range(len(a)):
        num_list = a[::]
        num_list[i] = x
        result = max(result, func(num_list))

    print(result)