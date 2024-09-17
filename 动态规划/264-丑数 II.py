def nthUglyNumber(n: int) -> int:
    result = [1] * n

    a = b = c = 0

    for i in range(1, n):
        num_a = result[a] * 2
        num_b = result[b] * 3
        num_c = result[c] * 5

        result[i] = min(num_a, num_b, num_c)

        if result[i] == num_a:
            a += 1
        if result[i] == num_b:
            b += 1
        if result[i] == num_c:
            c += 1

    return result[-1]
