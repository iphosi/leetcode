def func(n, k):
    nums = [i for i in range(1, n + 1)]

    i = n - 1

    result = []

    while k >= i and nums:
        result.append(nums.pop())
        k -= i
        i -= 1

    if nums:
        result.append(nums.pop(k))

    result.extend(nums)

    return result
