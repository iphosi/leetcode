from typing import List


def nthSuperUglyNumber(n: int, primes: List[int]) -> int:
    result = [1] * n
    pointers = [0] * len(primes)

    for i in range(1, n):
        result[i] = min(
            result[pointers[j]] * primes[j]
            for j in range(len(primes))
        )
        for j in range(len(primes)):
            if result[i] == result[pointers[j]] * primes[j]:
                pointers[j] += 1

    return result[-1]
