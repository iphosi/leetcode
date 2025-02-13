from typing import List


# dp_reg[i]: 通过 regular 路线到达 i 的最小花费
# dp_exp[i]: 通过 express 路线到达 i 的最小花费


def minimumCosts(regular: List[int], express: List[int], expressCost: int) -> List[int]:
    n = len(regular)
    dp_reg = [0] * n
    dp_exp = [0] * n

    dp_reg[0] = regular[0]
    dp_exp[0] = express[0] + expressCost

    cost = [0] * n
    cost[0] = min(dp_reg[0], dp_exp[0])

    for i in range(1, n):
        dp_reg[i] = min(dp_reg[i - 1], dp_exp[i - 1]) + regular[i]
        dp_exp[i] = min(dp_reg[i - 1] + expressCost, dp_exp[i - 1]) + express[i]
        cost[i] = min(dp_reg[i], dp_exp[i])

    return cost


result = minimumCosts(regular = [1,6,9,5], express = [5,2,3,10], expressCost = 8)

pass