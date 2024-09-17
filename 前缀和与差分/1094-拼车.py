from typing import List


# 差分：用于高效地为区间 [l, r] 内的数统一加上一个数
# diff[0] = nums[0]
# diff[i] = nums[i] - nums[i - 1]
# diff[l] + k 等价于对 nums[l:] 统一加上 k
# diff[r + 1] - k 等价于对 nums[r + 1:] 统一减去 k
# 使用以上两操步作后，对 diff 数组求前缀和，即可实现对 nums 区间 [l, r] 内的数统一加上 k 的操作


def carPooling(trips: List[List[int]], capacity: int) -> bool:
    diff = [0] * 1001

    for trip in trips:
        diff[trip[1]] += trip[0]
        diff[trip[2]] -= trip[0]  # 到达终点就下车，因此是在 [trip[1], trip[2] - 1] 区间内加上乘客数量

    prefix = 0

    for num in diff:
        prefix += num
        if prefix > capacity:
            return False

    return True
