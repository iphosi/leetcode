from collections import Counter
import heapq
from typing import List
import random


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count_dict = Counter(nums)

    heap = []
    for num, count in count_dict.items():
        heapq.heappush(heap, [count, num])
        if len(heap) > k:
            heapq.heappop(heap)

    return [item[1] for item in heap]

# 快排解法
# 1. 记录每个数字出现的次数
# 2. 对每个数及对应次数通过快排进行排序，返回前k个
# 3. 快排步骤
#    i. 随机选一个中间值作为基准，并把它挪到最左侧
#    ii. 从第2个元素开始遍历，遍历过程中，要把比基准大的挪到左边，比基准小的挪到右边
#    iii. i 指向比基准大的元素，只要 j 指向的元素比基准小，就把 j 位置的元素和i后面一个位置的元素对调
#    并且i后移一位，这样 i 指向的元素以及i之前的元素都是比基准大的元素（基准本身除外）
#    iv. j遍历到末尾后，此时i指向的就是排序后的列表中比基准大的最后一个元素，将该元素和基准对调，即
#    num_cnt[low], num_cnt[i] = num_cnt[i], num_cnt[low]
#    这样排序后的列表就是在i位置前的都比 i 大，i 位置后的都比 i 小
# 4. 接下来就是分治部分了
#    i. 如果 i == k - 1，也就是i及之前的元素恰好组成了我们想要的topK，直接返回前k个元素
#    ii. 如果 i > k - 1, 也就是i及之前的元素组成了top(K+N)，要对前 i 个元素再进行一次快排，从top(K+N)里选出topK
#    findTopK(num_cnt, k, low, i - 1)
#    iii. 如果 i < k - 1，也就是i及之前的元素组成了top(K-N)，要对i之后的元素再进行快排，在之后的元素中选出topN
#    findTopK(num_cnt, k, i + 1, high)
# 5. 返回快排结果中的数字部分

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        num_cnt = list(count.items())
        topKs = self.findTopK(num_cnt, k, 0, len(num_cnt) - 1)
        return [item[0] for item in topKs]

    def findTopK(self, num_cnt, k, start, end):
        rand_idx = random.randint(start, end)
        num_cnt[start], num_cnt[rand_idx] = num_cnt[rand_idx], num_cnt[start]

        p = start
        j = start + 1
        for i in range(start + 1, end + 1):
            if num_cnt[i][1] >= num_cnt[p][1]:
                num_cnt[i], num_cnt[j] = num_cnt[j], num_cnt[i]
                j += 1

        num_cnt[p], num_cnt[j - 1] = num_cnt[j - 1], num_cnt[p]

        if j == k:
            return num_cnt[:k]
        elif j > k:
            return self.findTopK(num_cnt, k, start, j - 2)
        else:
            return self.findTopK(num_cnt, k, j, end)
