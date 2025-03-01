from typing import List


def rotate(nums: List[int], k: int) -> None:
    def reverse(i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    n = len(nums)
    k %= n  # 轮转 k 次等于轮转 k % n 次
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
