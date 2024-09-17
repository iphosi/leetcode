from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    idx = 0
    gain = 0

    for i in range(len(gas)):
        gain += (gas[i] - cost[i])
        if gain < 0:
            idx = i + 1
            gain = 0

    return idx
