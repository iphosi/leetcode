def mySqrt(x: int) -> int:
    result = None
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2

        if mid ** 2 <= x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
